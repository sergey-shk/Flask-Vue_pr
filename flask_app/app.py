from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, session, User


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'i used to be an adventurer like you..'

cors = CORS(app, resources={r'*': {'origins': '*'}})

# Database migrations
#migrate = Migrate(app, db)
# Use:
# db migrate -m 'Initial migtation.'
# db upgrade


@app.route('/api/users/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True)
    username = data['username']
    hash_pass = generate_password_hash(data['password'])
    new_user = User(username=username, password=hash_pass)
    session.add(new_user)
    session.commit()

    if new_user != None:
        user = User.autheticate(**data)
        if user != None:
            access_token(identity=data['username'])
            res = {
                'msg': 'ok',
                'token': access_token,
                'id': user.id,
                'username': user.username,
                'date_of_birth': user.date_of_birth
            }
            return jsonify(res), 200
    return jsonify({'msg': 'Error'}), 401


@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = User.autheticate(**data)
    if user is None:
        return jsonify({'msg': 'Error'}), 401
    access_token = create_access_token(identity=data['username'])
    res = {
        'msg': 'ok',
        'token': access_token,
        'id': user.id,
        'username': user.username,
        'date_of_birth': user.date_of_birth
    }
    return jsonify(res), 200
















if __name__ == 'main':
    app.run(debug=True)
