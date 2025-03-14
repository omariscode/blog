from models.schema import Reactions
from dao.reaction_dao import ReactionDAO

class ReactionService:
    @staticmethod
    def register_reaction(user_id:int, post_id:int, react:bool):
        reaction = Reactions(user_id=user_id, post_id=post_id, react=react)
        return ReactionDAO.add_reaction(reaction)
    
    @staticmethod
    def get_reaction_by_post_id(post_id):
        return ReactionDAO.get_reaction_by_post_id(post_id)
    
    @staticmethod
    def get_reactin_by_id(id):
        return ReactionDAO.get_reaction_by_id(id)
    
    @staticmethod
    def delete_reaction(id):
        return ReactionDAO.delete_reaction(id)