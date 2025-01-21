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
    
    def load_questions(file_path):
     with open(file_path, 'r') as file:
        return json.load(file)

def quiz_user(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
            
        answer = None
        
        timer = threading.Timer(30.0, lambda: None)
        timer.start()
        start_time = time.time()
        
        while time.time() - start_time < 30 and answer is None:
            answer = input("Your answer (a/b/c/d): ")
         
        timer.cancel()
        if answer == question["answer"]:
            score += 1
        elif answer is None:
            print("Time's up! Moving to the next question.")
        start_time = time.time()
        
        print("You have 30 seconds to answer:")
        while time.time() - start_time < 30:
            if not answer:
                remaining_time = 30 - int(time.time() - start_time)
                print(f"Time remaining: {remaining_time} seconds", end="\r")
            else:
                answer = input("\nYour answer (a/b/c/d): ").strip().lower()
                timer.cancel()
            answer = input("\nYour answer (a/b/c/d): ").strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
        
        if not answer:
            print("\nTime's up! Moving to the next question.")
            start_time = time.time()
        elif answer == question["answer"]:
            print("Correct!")
            score += 12225
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    return score
