from src.database.config import supabase

import bcrypt


# function for hashing using bcrypt
def hash_pass(pwd):
    #                password           salt genrate
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

# Function to check password in login process
def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.code())

# function to check if username already taken
def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0  # this line returns 1(true) on if username matches

# function to create teacher
def create_teacher(username, password, name):
    data = {
        "username" : username,
        "password" : hash_pass(password), #hashing using bcrypt
        "name" : name
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data

#function for teacher login:
def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data(0)
        if check_pass(password, teacher["password"]):
            return teacher
    return None