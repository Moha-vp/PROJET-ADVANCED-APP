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

def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

      
def quiz_user(questions):
    score = 0
    total_questions = len(questions)
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total_questions}:")
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        answer = None
        start_time = time.time()
        timer = threading.Timer(30.0, lambda: print("\nTime's up!"))
        timer.start()
        
       
        while time.time() - start_time < 30:
            if not answer:
                remaining_time = 30 - int(time.time() - start_time)
                print(f"Time remaining: {remaining_time} seconds", end="\r")
                
                # Check for input with timeout
                try:
                    # Use a small timeout to allow for timer updates
                    answer = input("\nYour answer (a/b/c/d): ").strip().lower()
                    if answer in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        print("Invalid input. Please enter a, b, c, or d.")
                        answer = None
                except EOFError:
                    continue
            
        timer.cancel()
        
        # Handle answer checking
        if not answer or answer not in ['a', 'b', 'c', 'd']:
            print("\nTime's up! Moving to next question.")
            print(f"The correct answer was: {question['answer']}")
        else:
            if answer == question['answer']:
                score += 1
                print("\nCorrect! ✓")
            else:
                print(f"\nWrong! ✗ The correct answer was: {question['answer']}")
        
        # Add a small pause between questions
        if i < total_questions:
            print("\nNext question in 2 seconds...")
            time.sleep(2)
    
    # Calculate percentage
    percentage = (score / total_questions) * 100
    print(f"\nQuiz completed!")
    print(f"Final Score: {score}/{total_questions} ({percentage:.1f}%)")
    
    return score
 
       
    #----------------------------------------anis-------------------------------------------------------#
    # File Paths
users_file = "data/users.json"
questions_file = "data/questions.json"

# Load users and questions
users_data = load_users(users_file)
questions_data = load_questions(questions_file)

# Check if user exists
user_id = int(input("Enter your ID: "))
user = find_user(users_data, user_id)

if user:
    print(f"Welcome back, {user['name']}!")
    print("Your History:")
    for session in user["history"]:
        print(f"- Date: {session['date']}, Score: {session['score']}, Category: {session['category']}")
else:
    name = input("You are new here! Enter your name: ")
    user = add_new_user(users_data, user_id, name)
    print(f"Welcome, {name}! Your profile has been created.")
