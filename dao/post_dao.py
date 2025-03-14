from models.schema import Posts
from app import db

class PostDAO:
    @staticmethod
    def add_post(post):
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def get_posts():
        return Posts.query.order_by(Posts.created_at).all()

    @staticmethod
    def get_post_by_id(id):
        return Posts.query.get_or_404(id)   
    
    @staticmethod
    def update_post(id, title, description):
        post = PostDAO.get_post_by_id(id)
        if post:
            post.title = title
            post.description = description
            db.session.commit()
            return True
        return False
    
    @staticmethod 
    def delete_post(id):
        post = PostDAO.get_post_by_id(id)
        try:
            db.session.delete(post) 
            db.session.commit()
            return "Deleted with success"
        except Exception as e: 
            db.session.rollback()  
            return f"Error deleting post: {e}"