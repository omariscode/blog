from models.schema import Reactions
from app import db

class ReactionDAO:
    @staticmethod
    def add_reaction(reaction):
        db.session.add(reaction)
        db.session.commit()

    @staticmethod
    def get_reaction_by_post_id(post_id):
        return Reactions.query.filter_by(post_id=post_id).count()
    
    @staticmethod
    def get_reaction_by_id(id):
        return Reactions.query.filter_by(id=id).first()
    
    @staticmethod
    def delete_reaction(id):
        react = ReactionDAO.get_reaction_by_id(id)
        try:
            db.session.delete(react)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f'Error deleting reaction: {e}'