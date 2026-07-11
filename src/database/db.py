from src.database.config import supabase

import bcrypt

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