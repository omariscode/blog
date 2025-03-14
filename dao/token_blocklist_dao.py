from models.schema import TokenBlockList
from app import db

class TokenBlocklistDAO:
    @staticmethod
    def add_token(jti):
        db.session.add(TokenBlockList(jti=jti))
        db.session.commit()

    @staticmethod
    def is_token_blocked(jti):
        return db.session.query(TokenBlockList.id).filter_by(jti=jti).scalar() is not None