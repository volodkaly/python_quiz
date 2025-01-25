import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("300x200")

# Define the quiz questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid"], "correct": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "correct": "4"},
    {"question": "What is 2 + 3?", "options": ["3", "4", "5"], "correct": "5"},
    {"question": "What is the capital of Germany?", "options": ["Berlin", "Vienna", "Amsterdam"], "correct": "Berlin"}
]

# Initialize question index
current_question_index = 0

# Define a label to show feedback
feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

# Function to check answer
def check_answer(selected_option, button):
    correct_answer = questions[current_question_index]["correct"]
    
    if selected_option.strip().lower() == correct_answer.strip().lower():
        button.config(bg="green")  # Change button color to green if correct
        feedback_label.config(text="Correct!", fg="green")
    else:
        button.config(bg="red")  # Change button color to red if wrong
        feedback_label.config(text="Wrong!", fg="red")
        
        # Highlight the correct answer button in green
        for b in buttons:
            if b.cget("text") == correct_answer:
                b.config(bg="green")

    # Disable buttons after answering
    for b in buttons:
        b.config(state=tk.DISABLED)

    # Reset after a delay
    root.after(500, reset_buttons)

# Function to reset buttons and load next question
def reset_buttons():
    for b in buttons:
        b.config(bg="SystemButtonFace", state=tk.NORMAL)  # Reset color and enable buttons
    
    global current_question_index
    current_question_index = (current_question_index + 1) % len(questions)  # Cycle through questions
    
    load_question()

# Function to load question
def load_question():
    question_data = questions[current_question_index]
    question_label.config(text=question_data["question"])
    
    # Shuffle options to randomize their order
    shuffled_options = random.sample(question_data["options"], len(question_data["options"]))
    
    for i, option in enumerate(shuffled_options):
        buttons[i].config(text=option, command=lambda opt=option, btn=buttons[i]: check_answer(opt, btn))

# Create a label for the question
question_label = tk.Label(root, text="", wraplength=250, font=("Arial", 12))
question_label.pack(pady=10)

# Create buttons for each option
buttons = []
for _ in range(3):  # Assuming we have three options for each question
    button = tk.Button(root, text="", command=lambda opt=None: None)  # Placeholder command
    button.pack(pady=5)
    buttons.append(button)

# Load the first question
load_question()

# Run the application
root.mainloop()
