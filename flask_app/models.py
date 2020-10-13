
from sqlalchemy import Table, Boolean, Column, Integer, String, MetaData, create_engine, UniqueConstraint, Date
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


engine = create_engine('postgresql://postgres:admin@localhost/flask_app_db01')
if not database_exists(engine.url):
    create_database(engine.url)
db = declarative_base()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


class User(db):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    date_of_birth = Column(Date)
    admin_role = Column(Boolean, default=False)

    @classmethod
    def autheticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        if not username or not password:
            return None# return msg
        user = session.query(cls).filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None# -||-
        return user


db.metadata.create_all(engine)
