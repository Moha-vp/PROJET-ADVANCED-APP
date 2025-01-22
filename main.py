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

def add_new_user(users_data, user_id, name):
    new_user = {
        "id": user_id,
        "name": name,
        "history": []
    }
    users_data["users"].append(new_user)
    return new_user

def update_user_history(user, score, category):
    from datetime import datetime
    user["history"].append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "score": score,
        "category": category
    })
     # Select category
category = input("Choose a category (Algorithmique, Mathematique, Culture Générale,Intelligence Artificielle,Cyber Security): ")
questions = questions_data["categories"].get(category, [])

if not questions:
    print("Invalid category selected.")
else:
    score = quiz_user(questions)
    print(f"Your score: {score}/{len(questions)}")
    update_user_history(user, score, category)

# Save data
save_users(users_file, users_data)
