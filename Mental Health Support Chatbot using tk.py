import tkinter as tk
from tkinter import messagebox, scrolledtext
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot instance
mental_health_bot = ChatBot("SupportBot")

# Train chatbot with mental health responses
trainer = ListTrainer(mental_health_bot)
training_data = [
    "I'm feeling stressed", "Try deep breathing exercises and a short walk.",
    "I'm anxious", "Try grounding techniques like the 5-4-3-2-1 method.",
    "I'm sad", "Listen to uplifting music and talk to a close friend.",
    "I feel alone", "You are not alone. Connect with a loved one or try journaling.",
    "I feel demotivated", "Break your tasks into small steps and set achievable goals.",
    "Give me a positive quote", "You are stronger than you think. Keep going!",
    "How can I relax?", "Try meditation, journaling, or taking a break in nature."
]

trainer.train(training_data)

# GUI Application
class MentalHealthChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health Support Chatbot")
        self.root.geometry("500x500")

        tk.Label(self.root, text="💙 Mental Health Chatbot 💙", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Chatbox
        self.chatbox = scrolledtext.ScrolledText(self.root, width=50, height=15, wrap=tk.WORD, font=("Arial", 10))
        self.chatbox.pack(pady=5)
        self.chatbox.insert(tk.END, "Chatbot: Hello! How are you feeling today? 😊\n")
        
        # User input field
        self.user_input = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.user_input.pack(pady=5)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.get_response, font=("Arial", 12), bg="lightblue")
        self.send_button.pack(pady=5)

    def get_response(self):
        """Handles user input and chatbot response."""
        user_text = self.user_input.get()
        if user_text:
            self.chatbox.insert(tk.END, f"You: {user_text}\n")
            response = mental_health_bot.get_response(user_text)
            self.chatbox.insert(tk.END, f"Chatbot: {response}\n\n")
            self.user_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please type a message.")

# Run the chatbot GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = MentalHealthChatbot(root)
    root.mainloop()
