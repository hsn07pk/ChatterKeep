# README: Flask-Based Chatbot with Multi-User Session Management

## Overview
This project is a Flask-based chatbot application that supports multi-user session management and persistent conversations. It is designed to handle simultaneous users, track their sessions independently, and provide a seamless interaction experience.

---

## Features
1. **Greeting and Personalized Interaction**:
   - The chatbot begins by asking for the user's name and favorite song upon greeting with "hello".
   - Responds appropriately based on user inputs.

2. **Validation**:
   - Validates the first message to ensure it is "hello"; otherwise, returns an error message.

3. **Custom Session Management**:
   - Tracks user sessions without using cookies or Flask-Session.
   - Persists session data in an SQLite database for continuity.

4. **Single Endpoint**:
   - Interaction is handled through the `/chat` endpoint, accepting JSON payloads.

5. **Dockerized Deployment**:
   - The application is fully containerized for easy deployment.

---

## Technologies Used
- **Flask**: Web framework for building the API.
- **SQLite**: Lightweight database for session persistence.
- **Python**: Backend programming language.
- **Docker**: For containerization and deployment.

---

## Installation Instructions

### Prerequisites
- Python 3.9+
- Docker (for containerized deployment)

### Local Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Test the Endpoint**:
   Use a tool like Postman or `curl` to send requests to `http://127.0.0.1:5000/chat`.

   Example Request:
   ```json
   {
       "user_phone": "1234567890",
       "user_message": "hello"
   }
   ```

### Docker Setup
1. **Build the Docker Image**:
   ```bash
   docker build -f docker/Dockerfile -t flask-chatbot .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 flask-chatbot
   ```

3. **Test the Endpoint**:
   Access the API at `http://localhost:5000/chat`.

---

## Architecture
- **`app.py`**: Main Flask application.
- **`session_manager.py`**: Manages user sessions in memory and integrates with the database.
- **`db_handler.py`**: Handles SQLite interactions for session persistence.
- **`utils.py`**: Contains helper functions for validation and processing.
- **`Dockerfile`**: Configuration for containerizing the application.
- **`requirements.txt`**: Python dependencies.

---

## Example Interaction
### User 1:
**Request:**
```json
{
    "user_phone": "1111111111",
    "user_message": "hello"
}
```
**Response:**
```json
{
    "user_phone": "1111111111",
    "bot_message": "What is your name?"
}
```

**Request:**
```json
{
    "user_phone": "1111111111",
    "user_message": "John"
}
```
**Response:**
```json
{
    "user_phone": "1111111111",
    "bot_message": "Hello John, what is your favorite song?"
}
```

**Request:**
```json
{
    "user_phone": "1111111111",
    "user_message": "Bohemian Rhapsody"
}
```
**Response:**
```json
{
    "user_phone": "1111111111",
    "bot_message": "Playing Bohemian Rhapsody"
}
```

---

## Testing
1. **Simultaneous Users**:
   Ensure multiple users can interact with the bot independently by sending requests with different `user_phone` values.

2. **Edge Cases**:
   - Missing or invalid `user_phone` or `user_message` fields.
   - Unexpected user inputs.

---

## License
This project is licensed under the MIT License.

