import tkinter as tk
from tkinter import messagebox

class CareerChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Career Guidance Chatbot")
        self.root.geometry("500x400")

        self.stream = tk.StringVar()
        self.interest = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Creates the chatbot GUI layout."""
        tk.Label(self.root, text="Welcome to Career Guidance Chatbot!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text="Which stream did you take in Class 12?", font=("Arial", 12)).pack()

        # Stream selection
        streams = ["Science", "Commerce", "Arts"]
        for s in streams:
            tk.Radiobutton(self.root, text=s, variable=self.stream, value=s, font=("Arial", 10)).pack()

        tk.Button(self.root, text="Next", command=self.ask_interest, font=("Arial", 12), bg="lightblue").pack(pady=10)

    def ask_interest(self):
        """Asks for interest after selecting the stream."""
        if not self.stream.get():
            messagebox.showwarning("Warning", "Please select a stream.")
            return

        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"You selected {self.stream.get()}!", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.root, text="What are you most interested in?", font=("Arial", 12)).pack()

        # Interests based on stream
        interest_options = {
            "Science": ["Engineering", "Medical", "Research", "Technology"],
            "Commerce": ["Business", "Finance", "Accounting", "Marketing"],
            "Arts": ["Literature", "Media", "Psychology", "Law"]
        }

        for option in interest_options[self.stream.get()]:
            tk.Radiobutton(self.root, text=option, variable=self.interest, value=option, font=("Arial", 10)).pack()

        tk.Button(self.root, text="Get Career Options", command=self.show_careers, font=("Arial", 12), bg="lightgreen").pack(pady=10)

    def show_careers(self):
        """Shows career suggestions based on interests."""
        if not self.interest.get():
            messagebox.showwarning("Warning", "Please select an area of interest.")
            return

        careers = {
            "Engineering": ["Software Engineer", "Mechanical Engineer", "Civil Engineer"],
            "Medical": ["Doctor", "Dentist", "Pharmacist"],
            "Research": ["Scientist", "Lab Technician", "Biotechnologist"],
            "Technology": ["AI Specialist", "Data Scientist", "Cybersecurity Expert"],
            "Business": ["Entrepreneur", "Business Analyst", "Investment Banker"],
            "Finance": ["Chartered Accountant", "Financial Analyst", "Stock Trader"],
            "Accounting": ["Auditor", "Tax Consultant", "Forensic Accountant"],
            "Marketing": ["Digital Marketer", "Brand Manager", "Market Research Analyst"],
            "Literature": ["Writer", "Journalist", "Editor"],
            "Media": ["Filmmaker", "Photographer", "Social Media Manager"],
            "Psychology": ["Psychologist", "Counselor", "HR Specialist"],
            "Law": ["Lawyer", "Judge", "Legal Consultant"]
        }

        career_list = careers.get(self.interest.get(), ["No specific careers found."])
        career_text = "\n".join(career_list)

        messagebox.showinfo("Career Options", f"💡 Based on your interest in {self.interest.get()}, you can pursue:\n\n{career_text}")

# Run the chatbot
if __name__ == "__main__":
    root = tk.Tk()
    app = CareerChatbot(root)
    root.mainloop()
