from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS


DEBUG = True
app = Flask(app)
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "i used to be an adventurer like you..."
app.config['JWT_SECRET_KEY'] = '...then i took an arrow in the knee'
jwt = JWTManager(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})


if __name__ == '__main__':
    app.run(debug=DEBUG)
