from flask_jwt_extended import create_access_token, create_refresh_token, get_current_user
from dao.token_blocklist_dao import TokenBlocklistDAO

class AuthService:
    @staticmethod
    def create_tokens(identity, user_id):
        additional_claims = {"user_id": user_id}
        access_token = create_access_token(identity=identity, additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=identity)
        return access_token, refresh_token
        
    @staticmethod
    def revoke_token(jti):
        TokenBlocklistDAO.add_token(jti)

    @staticmethod
    def is_token_revoked(jti):
        return TokenBlocklistDAO.is_token_blocked(jti)