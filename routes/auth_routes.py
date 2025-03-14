from flask_mail import Message
from flask import request, jsonify
from services.user_service import UserService
from services.auth_service import AuthService
from app import jwt, app, bcrypt, serializer, mail
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

BASE_URL = 'http://127.0.0.1:2310'

@app.route('/api/register', methods=['POST'])
def register():
    name = request.form.get('name')
    username = request.form.get('username')
    mail = request.form.get('email')
    phone = request.form.get("phone")
    photo = request.files['photo']
    password = request.form.get('password')

    try:
        user = UserService.register_user(name, username, mail, phone, photo, password)
    except Exception as e:
        return jsonify({"error": f"Impossible to create account: {e}"}), 400
    
    return jsonify({"msg": "User created with sucess"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data['email']
    password= data['password']

    user = UserService.get_user_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password):
        acess_token, refresh_token = AuthService.create_tokens(identity=email, user_id=user.id)
        return jsonify(acess_token=acess_token, refresh_token=refresh_token), 200
    
    return jsonify({"msg": "Invalid email or password"}), 401

@app.route('/api/forget-pass', methods=['POST'])
def forget_pass():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"message": "Email é obrigatório!"}), 400

    user = UserService.get_user_by_email(email)
    if not user:
        return jsonify({"message": "Usuário não encontrado!"}), 404

    token = serializer.dumps(email, salt='password-reset')
    reset_link = f"{BASE_URL}/reset-password?token={token}"

    msg = Message('Redefinição de Senha', recipients=[email])
    msg.html = f"""<p>Para redefinir sua senha, clique no link: <a href="{reset_link}">Redefinir Senha</a></p>"""
    msg.body = f"Para redefinir sua senha, clique no link: {reset_link}"
    
    mail.send(msg)  

    return jsonify({"message": f"E-mail de recuperação enviado!: {reset_link}"}), 200

@app.route('/api/reset-password/<token>', methods=['POST'])
def reset_password(token):
    try:
        email = serializer.loads(token, salt='password-reset', max_age=1800)  
    except:
        return jsonify({"message": "Token inválido ou expirado!"}), 400

    data = request.get_json()
    
    if UserService.reset_password(email, data['new_password']):
        return jsonify({"message": "Senha alterada com sucesso!"}), 200
    
    return jsonify({"message": "Usuário não encontrado!"}), 404


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token, _ = AuthService.create_tokens(identity=identity)
    return jsonify(access_token=access_token)

@app.route("/api/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    AuthService.revoke_token(jti)
    return jsonify({"msg": "Token revoked"}), 200

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return AuthService.is_token_revoked(jti)