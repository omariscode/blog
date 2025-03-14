from dao.post_dao import PostDAO
from models.schema import Posts
from services.others_service import upload_post_to_cloudinary

class PostService:
    @staticmethod
    def register_post(title, description, cover, user_id):
        cloudinary_url = upload_post_to_cloudinary(cover)
        post = Posts(title=title, description=description, cover=cloudinary_url, user_id=user_id)
        return PostDAO.add_post(post)
    
    @staticmethod
    def get_post_by_id(id):
        return PostDAO.get_post_by_id(id)
    
    @staticmethod
    def get_posts():
        return PostDAO.get_posts()
    
    @staticmethod
    def get_post_by_id(id):
        return PostDAO.get_post_by_id(id)
    
    @staticmethod
    def update_post(title, description):
        return PostDAO.update_post(title, description)
    
    @staticmethod
    def delete_post(id):
        return PostDAO.delete_post(id)