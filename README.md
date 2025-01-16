# Quiz Application

This project is a quiz application that allows users to test their knowledge in various subjects. The application presents questions categorized into different subjects, collects user responses, calculates scores, and maintains a history of user attempts.

## Project Structure

- **data/questions.json**: Contains questions categorized into subjects such as "Algorithmique", "Mathematique", and "Culture Générale". Each question includes multiple options and the correct answer.
  
- **data/users.json**: Stores user data, including user ID, name, and history of quiz attempts. The history records the date, score, and category of each quiz taken by the user.

- **main.py**: The main script of the application. It handles user interaction, including:
  - Prompting the user for their ID
  - Checking if they are new or returning
  - Allowing them to select a category of questions
  - Presenting questions one by one
  - Collecting answers and calculating scores
  - Providing feedback
  - Updating user history

## Setup and Requirements

1. **Clone the repository**:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the project directory**:
   ```
   cd quiz-app
   ```

3. **Install dependencies**:
   Ensure you have Python installed. You may need to install any required packages using pip if specified in a requirements file.

4. **Run the application**:
   Execute the main script:
   ```
   python main.py
   ```

## Usage

- Upon running the application, users will be prompted to enter their ID. If they are new, they will be asked to provide their name.
- Users can select a category of questions to answer.
- After answering all questions, users will receive their score and feedback based on their performance.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.