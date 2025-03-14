from services.others_service import upload_photo_to_cloudinary
from email_validator import validate_email
from dao.user_dao import UserDAO
from models.schema import Users
from app import bcrypt

class UserService:
    @staticmethod
    def register_user(name, username, mail, phone, photo, password):
        password_hash = bcrypt.generate_password_hash(password)
        valid = validate_email(mail, check_deliverability=True)
        email = valid.email
        cloudinary_url = upload_photo_to_cloudinary(photo)
        user = Users(name=name, username=username, email=email, phone=phone, photo=cloudinary_url, password=password_hash)
        return UserDAO.add_user(user)
    
    @staticmethod
    def get_user_by_email(email):
        return UserDAO.get_user_by_email(email)
    
    @staticmethod
    def reset_password(email, new_password):
        return UserDAO.update_password(email, new_password)