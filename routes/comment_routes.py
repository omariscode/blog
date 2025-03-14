from services.comment_service import CommentService
from flask import request, jsonify
from app import app

@app.route('/api/add_comments', methods=['POST'])
def make_comment():
    data = request.get_json()

    user_id = data['me']
    post_id = data['his']
    content = data['content']

    try:
        comment = CommentService.register_comment(user_id, post_id, content)
    except Exception as e:
        return jsonify({"erro": f"Impossible to make comment: {e}"}), 401
    
    return jsonify({"msg": "Coment created with sucess"}), 201

@app.route('/api/get_comments/<int:post_id>', methods=['GET'])
def get_comment(post_id):
    comments = CommentService.get_comments_by_post_id(post_id)

    comments_list = [
        {
            "user_id": comment.user_id,
            "post_id": comment.post_id,
            "content": comment.content
        }

        for comment in comments
    ]

    return jsonify(comments_list), 200

@app.route('/api/update_comment/<int:id>', methods=['PUT'])
def update_comment(id):
    data = request.get_json()
    content = data['content']

    try:
        comment_up = CommentService.update_comment(id, content)
    except Exception as e:
        return jsonify({"error": f"Cant update this comment because: {e}"})
    
    return jsonify({"msg": "Updated with sucess"}), 201

@app.route('/api/delete_comment/<int:id>', methods=['DELETE'])
def delete_comment(id):
    return CommentService.delete_comment(id), 200