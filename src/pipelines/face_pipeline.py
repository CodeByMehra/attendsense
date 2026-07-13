# Face Image -> Face Detector (dlib) -> Shape Predictor(sp) and detect landmarks-> ResNet (facerec) 128D -> SVM Classifier 

import dlib
import numpy as np 
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource 
def load_dlib_models(): 
    detector = dlib.get_frontal_face_detector()
    
    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    
    return detector,sp,facerec


# function to get face embeddings:
def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)
    
    encodings = []
    
    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face__descriptor(image_np, shape, 1)
        
        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource  #used to run the followeing function one time only
def get_trained_model():
    X = []
    y = []
    
    student_db = get_all_students()
    
    if not student_db:
        return None
        
    for student in student_db:
        embedding = student.get("face_embedding")
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))
            
    if len(X) == 0:
        return 0
    
    #classifier
    clf= SVC(kernel="linear", probability=True, class_weight="balanced")
    
    try:
        clf.fit(X, y)
    except ValueError:
        pass
    return {"clf": clf, "X": X, "y": y}
    
    
def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np): # take photo or group photo as argument
    encodings = get_face_embeddings(class_image_np)  # get embeddings from the photo/ group photo
    
    detected_student = {}
    
    model_data = get_trained_model()
    
    if not model_data:
        return {}, [], 0  # {}- detected students, [] -> number of students, 0-> length of encodings
    
    clf = model_data["clf"]
    X= model_data["X"]
    y = model_data["y"]
    