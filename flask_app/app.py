from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, session, User, Post, likes_table


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'i used to be an adventurer like you..'
jwt = JWTManager(app)
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
            access_token = create_access_token(identity=data['username'])
            res = [{
                'msg': 'ok',
                'token': access_token,
                'id': user.id,
                'username': user.username,
                'date_of_birth': user.date_of_birth
            }]
            return jsonify(res), 200
    return jsonify({'msg': 'Error'}), 401


@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = User.autheticate(**data)
    if user is None:
        return jsonify({'msg': 'Error'}), 401
    access_token = create_access_token(identity=data['username'])
    res = [{
        'msg': 'ok',
        'token': access_token,
        'id': user.id,
        'username': user.username,
        'date_of_birth': user.date_of_birth
    }]
    return jsonify(res), 200


@app.route('/api/posts/createpost', methods=['POST'])
@jwt_required
def create_post():
    current_user = session.query(User).filter_by(username=get_jwt_identity()).first()
    if current_user == None:
        return jsonify("We don't recognize you...(-_-)")
    else:
        data = request.get_json(force=True)
        new_post = Post(body=data['body'], author_id=current_user.id)
        if new_post != None:
            session.add(new_post)
            session.commit()
            return jsonify(msg='Posted!')
        else:
            jsonify(msg='Something went wrong...(-__-)')


@app.route('/api/posts/getposts', methods=['GET'])
@jwt_required
def get_posts():
    current_user = session.query(User).filter_by(username=get_jwt_identity()).first()
    if current_user == None:
        return jsonify("Who you are?...(-_-)")
    else:
        posts = session.query(Post).all()
        if posts == None:
            return jsonify(msg='(sounds of crickets)')
        else:
            posts_s = [post.serialize() for post in posts]
            return jsonify(posts=posts_s)


@app.route('/api/posts/like', methods=['POST'])
@jwt_required
def post_like():
    current_user = session.query(User).filter_by(username=get_jwt_identity()).first()
    if current_user == None:
        return jsonify("Who you are?...(-_-)")
    else:
        data = request.get_json(force=True)
        #data['post_id']
        post = session.query(Post).filter_by(id=data['post_id']).first()
        post.liked_users.append(current_user)
        return jsonify(msg='Like that!')

if __name__ == '__main__':
    app.run(debug=True)
