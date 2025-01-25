import tkinter as tk
import random
import time

# Create the main window
root = tk.Tk()
root.title("Quiz App")


# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to 60% of the screen width and center it
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)  # You can adjust this as needed

# Calculate the position to center the window
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set the window geometry
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

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

# Define a label for the timer (elapsed time)
elapsed_time_label = tk.Label(root, text="Elapsed Time: 0s", font=("Arial", 12))
elapsed_time_label.pack(pady=10)

# Initialize start time
start_time = time.time()

# Function to update the elapsed time
def update_elapsed_time():
    elapsed_time = int(time.time() - start_time)  # Calculate elapsed time in seconds
    elapsed_time_label.config(text=f"Time: {elapsed_time}s")
    root.after(1000, update_elapsed_time)  # Call this function every second

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
        b.config(bg="lightgray", state=tk.NORMAL)  # Reset color and enable buttons
    
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

# Start the timer for tracking elapsed time
update_elapsed_time()

# Run the application
root.mainloop()
