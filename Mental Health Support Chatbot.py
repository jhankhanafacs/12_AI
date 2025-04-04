import tkinter as tk
from tkinter import messagebox

class MentalHealthChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health Support Chatbot")
        self.root.geometry("500x400")

        self.mood = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Creates the chatbot interface."""
        tk.Label(self.root, text="💙 Mental Health Support Chatbot 💙", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text="How are you feeling today?", font=("Arial", 12)).pack()

        # Mood selection
        moods = ["Stressed", "Anxious", "Sad", "Demotivated", "Happy"]
        for m in moods:
            tk.Radiobutton(self.root, text=m, variable=self.mood, value=m, font=("Arial", 10)).pack()

        tk.Button(self.root, text="Get Support", command=self.provide_support, font=("Arial", 12), bg="lightblue").pack(pady=10)

    def provide_support(self):
        """Provides mental health support based on mood."""
        if not self.mood.get():
            messagebox.showwarning("Warning", "Please select how you're feeling.")
            return

        responses = {
            "Stressed": "😌 Take a deep breath. Try the 4-7-8 breathing technique: Inhale for 4 seconds, hold for 7 seconds, and exhale for 8 seconds. Also, take a short walk to refresh your mind. 🧘",
            "Anxious": "🌿 Try grounding techniques: Look around and name 5 things you see, 4 things you feel, 3 things you hear, 2 things you smell, and 1 thing you taste. It helps bring you to the present moment. 🕊️",
            "Sad": "💛 It's okay to feel sad. Try listening to your favorite music, journaling your thoughts, or watching something that makes you laugh. Talking to a friend can also help. 🌸",
            "Demotivated": "🚀 Remember why you started! Break big goals into small steps. Reward yourself for small achievements. You’re doing better than you think! 💪",
            "Happy": "😊 That’s great! Spread positivity—send a kind message to someone, take a moment to appreciate yourself, and keep up the good vibes! ✨"
        }

        messagebox.showinfo("Support Message", responses[self.mood.get()])

# Run the chatbot
if __name__ == "__main__":
    root = tk.Tk()
    app = MentalHealthChatbot(root)
    root.mainloop()
