from flask import Flask, request, jsonify
from libs.session_manager import SessionManager
from libs.db_handler import DatabaseHandler
from libs.utils import validate_input, process_greeting

app = Flask(__name__)
session_manager = SessionManager()
db_handler = DatabaseHandler("sessions.db")

@app.route('/chat', methods=['POST'])
def chat():
    # Parse request payload
    data = request.get_json()
    user_phone = data.get('user_phone')
    user_message = data.get('user_message')

    if not user_phone or not user_message:
        return jsonify({"error": "Invalid input. 'user_phone' and 'user_message' are required."}), 400

    # Retrieve or create session
    session = session_manager.get_session(user_phone, db_handler)

    # Validate initial input if no session state exists
    if session['state'] == "start":
        if not validate_input(user_message):
            return jsonify({"user_phone": user_phone, "bot_message": "Invalid initial input, please say hello."})

        # Process greeting
        bot_message, next_state = process_greeting(user_message)
        session['state'] = next_state
        session_manager.update_session(user_phone, session, db_handler)
        return jsonify({"user_phone": user_phone, "bot_message": bot_message})

    # Handle ongoing conversation
    if session['state'] == "ask_name":
        session['name'] = user_message
        session['state'] = "ask_song"
        bot_message = f"Hello {user_message}, what is your favorite song?"
        session_manager.update_session(user_phone, session, db_handler)
        return jsonify({"user_phone": user_phone, "bot_message": bot_message})

    if session['state'] == "ask_song":
        session['favorite_song'] = user_message
        session['state'] = "done"
        bot_message = f"Playing {user_message}"
        session_manager.update_session(user_phone, session, db_handler)
        return jsonify({"user_phone": user_phone, "bot_message": bot_message})

    # Default case
    return jsonify({"user_phone": user_phone, "bot_message": "Thank you for using the chatbot!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)