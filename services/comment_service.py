from dao.comments_dao import CommentDAO
from models.schema import Comments

class CommentService:
    @staticmethod
    def register_comment(user_id, post_id, content):
        comment = Comments(user_id=user_id, post_id=post_id, content=content)
        return CommentDAO.add_comment(comment)
    
    @staticmethod
    def get_comments_by_post_id(post_id):
        return CommentDAO.get_comments_by_post_id(post_id)
    
    @staticmethod
    def get_comment_by_id(id):
        return CommentDAO.get_comment_by_id(id)
    
    @staticmethod
    def update_comment(id, content):
        return CommentDAO.update_comment(id, content)
        
    @staticmethod
    def delete_comment(id):
        return CommentDAO.delete_comment(id)        