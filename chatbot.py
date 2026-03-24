import nltk

# Define some sample patterns and responses
patterns = {
    'greeting': ["hello", "hi", "howdy"],
    'goodbye': ["bye", "farewell"],
    'thanks': ["thank you", "thanks"]
}

responses = {
    'greeting': "Hello! How can I assist you today?",
    'goodbye': "Goodbye! Have a great day!",
    'thanks': "You're welcome! If you have any more questions, feel free to ask."
}

# Function to match patterns
def match_pattern(user_input):
    for key in patterns:
        for pattern in patterns[key]:
            if pattern in user_input.lower():
                return key
    return None

# Simple chatbot loop
if __name__ == '__main__':
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(responses['goodbye'])
            break
        match = match_pattern(user_input)
        if match:
            print(f"Bot: {responses[match]}")
        else:
            print("Bot: I'm sorry, I didn't understand that.")