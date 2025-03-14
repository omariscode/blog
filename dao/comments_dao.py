from models.schema import Comments
from app import db

class CommentDAO:
    @staticmethod
    def add_comment(comment):
        db.session.add(comment)
        db.session.commit()

    @staticmethod
    def get_comments_by_post_id(post_id):
           return Comments.query.filter_by(post_id=post_id).all()
    
    @staticmethod
    def get_comment_by_id(id):
        return Comments.query.get_or_404(id)
    
    @staticmethod
    def update_comment(id, content):
        comment = CommentDAO.get_comment_by_id(id)
        if comment:
            comment.content = content
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def delete_comment(id):
        comment = CommentDAO.get_comment_by_id(id)
        try:
            db.session.delete(comment)
            db.session.commit()
            return 'Deleted with sucess'
        except Exception as e:
            db.session.rollback()
            return f"Error deleting comment: {e}"