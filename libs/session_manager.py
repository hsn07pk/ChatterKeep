class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_session(self, user_phone, db_handler):
        session = db_handler.get_session(user_phone)
        if not session:
            session = {"state": "start"}
            db_handler.save_session(user_phone, session)
        return session

    def update_session(self, user_phone, session, db_handler):
        db_handler.save_session(user_phone, session)