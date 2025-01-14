# Comprehensive Python Quiz Game

# Step 1: Welcome the User
# This line demonstrates the use of the `input` function to take user input and store it in a variable, which is a fundamental way to interact with users.
name = input("Welcome! What's your name? ")
# This line shows how to use f-strings for string interpolation, combining variables with text for formatted output.
print(f"Hello, {name}! Let's start the quiz.\n")

# Step 2: Create the Quiz Questions
# This dictionary `quiz` uses key-value pairs to store questions as keys and their correct answers as values, demonstrating how to organize related data.
quiz = {
    "What is the capital of France?": "a",
    "Which programming language is known for its simplicity?": "b",
    "What is 5 + 7?": "c",
}

# This dictionary `options` maps each question to its multiple-choice options, showing another use of dictionaries to store related data.
options = {
    "What is the capital of France?": "a) Paris\nb) London\nc) Berlin",
    "Which programming language is known for its simplicity?": "a) Java\nb) Python\nc) C++",
    "What is 5 + 7?": "a) 10\nb) 11\nc) 12",
}

# Step 3: Ask Questions in a Loop
score = 0

# This `for` loop iterates over the `quiz` dictionary, illustrating how to loop through key-value pairs in a dictionary using the `.items()` method.
for question, correct_answer in quiz.items():
    print(question)
    print(options[question])
    # This line demonstrates the use of the `input` function to take the user's answer and convert it to lowercase.
    answer = input("Your answer (a/b/c): ").lower()

    # This `if` statement checks if the user's answer matches the correct answer, demonstrating conditional logic.
    if answer == correct_answer:
        print("Correct!\n")
        # This line increments the score, showing how to use variables to track progress or state in a program.
        score += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")

# Step 4: Calculate the Score and Display Results
# This line provides output to indicate the end of the quiz, a good practice for user feedback.
print("Quiz Complete!")
# This line demonstrates the use of f-strings to include variable data in the output message.
print(f"Your final score is {score}/{len(quiz)}.\n")

# This `if` block demonstrates conditional logic to provide different feedback based on the user's performance.
if score == len(quiz):
    print(f"Amazing, {name}! You got a perfect score!")
elif score > len(quiz) / 2:
    print(f"Good job, {name}! You did well!")
else:
    print(f"Don't worry, {name}, keep practicing and you'll improve!")
