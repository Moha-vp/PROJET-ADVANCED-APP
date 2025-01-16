import json
import threading
import time
def load_users(file_path):

    with open(file_path, 'r') as file:
        return json.load(file)

def save_users(file_path, data):
 
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_user(users_data, user_id):
    for user in users_data["users"]:
        if user["id"] == user_id:
            return user
    return None