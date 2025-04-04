def suggest_outfit(event, weather, time_of_day):
    outfits = {
        "casual": {
            "hot": "Wear a cotton dress or light kurti with leggings. ☀️",
            "cold": "Wear jeans with a full-sleeve top and a cozy jacket. 🧥",
            "rainy": "Wear a waterproof jacket with comfy sneakers. ☔"
        },
        "formal": {
            "hot": "Wear a light saree or a formal kurti with palazzo pants. 🌞",
            "cold": "Wear a silk saree or a formal suit with a blazer. ❄️",
            "rainy": "Wear a formal dress with a raincoat and closed shoes. 🌧️"
        },
        "party": {
            "hot": "Wear a stylish dress or a trendy jumpsuit. 🎉",
            "cold": "Wear an elegant dress with a warm shawl. 🔥",
            "rainy": "Wear a knee-length dress with waterproof heels. 💃"
        },
        "wedding": {
            "hot": "Wear a lightweight saree or an anarkali suit. 💛",
            "cold": "Wear a heavy silk saree or a lehenga with a warm shawl. ❤️",
            "rainy": "Wear a georgette saree or salwar suit with waterproof footwear. 💐"
        }
    }
    
    return outfits.get(event, {}).get(weather, "Wear something comfortable and stylish! 😊") + (
        " Opt for bright colors in the day. 🌞" if time_of_day == "day" else " Choose darker shades for the evening. 🌙"
    )

def chatbot():
    print("👗 Hello! I'm your outfit suggestion chatbot.")
    
    while True:
        event = input("What is the event? (Casual/Formal/Party/Wedding or 'exit' to quit): ").strip().lower()
        if event == 'exit':
            print("Goodbye! Stay stylish! 💃")
            break
        
        weather = input("How is the weather? (Hot/Cold/Rainy): ").strip().lower()
        time_of_day = input("Is it Day or Night? ").strip().lower()
        
        outfit_suggestion = suggest_outfit(event, weather, time_of_day)
        print(f"👗 Outfit Suggestion: {outfit_suggestion}\n")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
