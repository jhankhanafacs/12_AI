import tkinter as tk
from tkinter import messagebox

class PersonalityChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Personality Type Chatbot")
        self.root.geometry("500x400")

        # Questions and answer choices
        self.questions = [
            ("How do you prefer to spend your free time?", ("Extroverted (E)", "E"), ("Introverted (I)", "I")),
            ("How do you make decisions?", ("Thinking (T)", "T"), ("Feeling (F)", "F")),
            ("How do you plan your day?", ("Judging (J)", "J"), ("Perceiving (P)", "P")),
            ("How do you handle social situations?", ("Sensing (S)", "S"), ("Intuitive (N)", "N"))
        ]

        self.current_question = 0
        self.answers = []
        self.var1 = tk.IntVar(value=0)  # Fix: Start unchecked
        self.var2 = tk.IntVar(value=0)

        self.create_widgets()

    def create_widgets(self):
        """Creates the question label and checkboxes."""
        self.question_label = tk.Label(self.root, text=self.questions[self.current_question][0], font=("Arial", 12), wraplength=400)
        self.question_label.pack(pady=20)

        # Checkbuttons (Checkboxes)
        self.option1 = tk.Checkbutton(self.root, text=self.questions[self.current_question][1][0], variable=self.var1, font=("Arial", 10))
        self.option1.pack()

        self.option2 = tk.Checkbutton(self.root, text=self.questions[self.current_question][2][0], variable=self.var2, font=("Arial", 10))
        self.option2.pack()

        # Next button
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12), bg="lightblue")
        self.next_button.pack(pady=20)

    def next_question(self):
        """Stores answer and moves to the next question."""
        selected = []
        if self.var1.get():
            selected.append(self.questions[self.current_question][1][1])  # Store selected value
        if self.var2.get():
            selected.append(self.questions[self.current_question][2][1])

        if not selected:  # If nothing is selected
            messagebox.showwarning("Warning", "Please select at least one option before proceeding.")
            return

        self.answers.append(selected[0])  # Store only one answer per question
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question][0])
            self.option1.config(text=self.questions[self.current_question][1][0])
            self.option2.config(text=self.questions[self.current_question][2][0])
            self.var1.set(0)  # Reset checkbox state
            self.var2.set(0)
        else:
            self.show_result()

    def show_result(self):
        """Displays the final personality type."""
        personality_type = "".join(self.answers)

        insights = {
            "ENTP": "You are an enthusiastic and curious debater! 🗣️",
            "INFJ": "You are an insightful and thoughtful visionary! 🌟",
            "ISFP": "You are a creative and independent artist! 🎨",
            "ESTJ": "You are a practical and organized leader! 📋",
            "INTP": "You are a logical and deep thinker! 🧠"
        }

        result_message = insights.get(personality_type, "You have a unique personality! 😊")
        messagebox.showinfo("Your Personality Type", f"✨ Your Personality Type: {personality_type} ✨\n\n{result_message}")

        self.root.quit()  # Close the application after showing results

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityChatbot(root)
    root.mainloop()
