from services.post_service import PostService
from flask_jwt_extended import jwt_required
from flask import request,jsonify
from app import app

@app.route('/api/add_post', methods=['POST'])
def add_post():
    user_id = request.form.get('user')
    title = request.form.get('title')
    description = request.form.get('desc')
    cover = request.files['cover']

    try:
        post = PostService.register_post(title, description, cover, user_id)
    except Exception as e:
        return jsonify({"error": f"Impossible to make post: {e}"}), 401
    
    return jsonify({"msg": "Post created with sucess"}), 201

@app.route('/api/get_posts', methods=['GET'])
def get_posts():
    posts = PostService.get_posts()

    posts_list = [
        {
            "title": post.title,
            "description": post.description,
            "cover": post.cover,
            "created_at": post.created_at
        }
        for post in posts
    ]

    return jsonify(posts_list), 200

@app.route('/api/get_post/<int:id>', methods=['GET'])
def get_post(id):
    post = PostService.get_post_by_id(id)

    post_info = {
        "title": post.title,
        "description": post.description,
        "cover": post.cover
    }

    return jsonify(post_info), 200

@app.route('/api/update_post/<int:id>', methods=['PUT'])
def update_post(id):
    post = PostService.get_post_by_id(id)

    data = request.get_json()
    title = data['title']
    description = data['desc']

    try:
        post_up = PostService.update_post(title, description)
    except Exception as e:
        return jsonify({"error": f"Error updating post: {e}"}), 401
    
    return jsonify({"msg": "Post updated with sucess"}), 201

@app.route('/api/delete_post/<int:id>', methods=['DELETE'])
def delete_post(id):
    return PostService.delete_post(id), 200