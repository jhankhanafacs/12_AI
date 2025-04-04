def get_class(percentage):
    if percentage >= 75:
        return "First Class with Distinction 🏆"
    elif percentage >= 60:
        return "First Class 🎖️"
    elif percentage >= 50:
        return "Second Class 🏅"
    elif percentage >= 35:
        return "Pass Class ✅"
    else:
        return "Fail ❌"

def chatbot():
    print("Hello! I'm your percentage classification chatbot 🤖")
    
    while True:
        user_input = input("Enter your percentage (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day! 😊")
            break
        
        try:
            percentage = float(user_input)
            if 0 <= percentage <= 100:
                classification = get_class(percentage)
                print(f"Your class: {classification}")
            else:
                print("Please enter a valid percentage between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric percentage.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
