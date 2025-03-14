from models.schema import Users
from app import bcrypt
from app import db

class UserDAO:
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
        
    @staticmethod
    def get_user_by_email(email):
        return Users.query.filter_by(email=email).first()
    
    @staticmethod
    def update_password(email, new_password):
        user = UserDAO.get_user_by_email(email)
        if user:
            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            db.session.commit()
            return True
        return False
