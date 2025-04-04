def ask_question(question, option1, option2):
    """Ask a question and return the personality trait based on the user's answer."""
    while True:
        answer = input(f"\n{question}\n1. {option1}\n2. {option2}\nChoose (1 or 2): ").strip()
        if answer == "1":
            return option1[0]  # First letter of option1
        elif answer == "2":
            return option2[0]  # First letter of option2
        else:
            print("Invalid input! Please enter 1 or 2.")

def chatbot():
    print("🤖 Welcome to the Personality Type Chatbot!")
    print("Answer the following questions to determine your personality type.\n")
    
    personality = ""
    personality += ask_question("How do you prefer to spend your free time?", "Going out with friends (E)", "Staying alone or with close friends (I)")
    personality += ask_question("How do you make decisions?", "Based on logic and facts (T)", "Based on emotions and feelings (F)")
    personality += ask_question("How do you plan your day?", "I prefer a structured plan (J)", "I go with the flow (P)")
    personality += ask_question("How do you handle social situations?", "I enjoy social gatherings (S)", "I prefer deep one-on-one conversations (N)")
    
    print(f"\n✨ Your Personality Type: **{personality}** ✨")
    
    # Giving brief personality insights
    insights = {
        "ENTP": "You are an enthusiastic and curious debater! 🗣️",
        "INFJ": "You are an insightful and thoughtful visionary! 🌟",
        "ISFP": "You are a creative and independent artist! 🎨",
        "ESTJ": "You are a practical and organized leader! 📋",
        "INTP": "You are a logical and deep thinker! 🧠",
    }
    
    print(insights.get(personality, "You have a unique personality! 😊"))

# Run the chatbot
if __name__ == "__main__":
    chatbot()
