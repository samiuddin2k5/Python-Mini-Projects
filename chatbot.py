def chatbot():
    print(" Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("ChatBot: Goodbye!")
            break
        elif 'hello' in user_input:
            print("ChatBot: Hi there!")
        elif 'how are you' in user_input:
            print("ChatBot: I'm good, thanks! How about you?")
        elif 'your name' in user_input:
            print("ChatBot: I'm your friendly chatbot!")
        elif 'help' in user_input:
            print("ChatBot: Try asking about my name or say hello!")
        else:
            print("ChatBot: Sorry, I didn't understand that.")

chatbot()
