import sqlite3
import json

class DatabaseHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    user_phone TEXT PRIMARY KEY,
                    session_data TEXT
                )
            ''')
            conn.commit()

    def get_session(self, user_phone):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT session_data FROM sessions WHERE user_phone = ?', (user_phone,))
            row = cursor.fetchone()
            if row:
                return json.loads(row[0])
            return None

    def save_session(self, user_phone, session):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            session_data = json.dumps(session)
            cursor.execute('''
                INSERT INTO sessions (user_phone, session_data)
                VALUES (?, ?)
                ON CONFLICT(user_phone) DO UPDATE SET session_data = ?
            ''', (user_phone, session_data, session_data))
            conn.commit()
