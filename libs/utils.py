def validate_input(user_message):
    return user_message.strip().lower() == "hello"

def process_greeting(user_message):
    if user_message.strip().lower() == "hello":
        return "What is your name?", "ask_name"
    return "Invalid input", "start"