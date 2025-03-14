from services.reaction_service import ReactionService
from flask import request, jsonify
from app import app

@app.route('/api/react', methods=['POST'])
def make_reaction():
    data = request.get_json()

    user_id = data['me']
    post_id = data['his']
    react = data['react']

    try:
        reaction = ReactionService.register_reaction(user_id, post_id, react)
    except Exception as e:
        return jsonify({"error": f"Impossible to react because: {e}"}), 401
    
    return jsonify({"msg": "Reaction added with sucess"}), 200

@app.route("/api/get_reactions/<int:post_id>", methods=['GET'])
def get_post_reactions(post_id):
    reactions = ReactionService.get_reaction_by_post_id(post_id)

    # reactions_list = [
    #     {
    #         "user_id": react.user_id,
    #         "post_id": react.post_id,
    #         "react": react.react
    #     }

    #     for react in reactions
    # ]

    return jsonify(reactions), 200

@app.route('/api/delete_reactions/<int:id>', methods=['DELETE'])
def delete_reactions(id):
    return ReactionService.delete_reaction(id)