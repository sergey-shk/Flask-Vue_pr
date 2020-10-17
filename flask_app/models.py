
from sqlalchemy import Table, Boolean, Column, Integer, String, MetaData, create_engine, UniqueConstraint, DateTime, ForeignKey, Date
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


engine = create_engine('postgresql://postgres:admin@localhost/flask_app_db03')
if not database_exists(engine.url):
    create_database(engine.url)
db = declarative_base()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


likes_table = Table('association',db.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('posts_id', Integer, ForeignKey('posts.id')))


class User(db):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    date_of_birth = Column(Date)
    admin_role = Column(Boolean, default=False)
    posts = relationship('Post')
    liked_posts = relationship('Post', secondary=likes_table, back_populates='liked_users')

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


class Post(db):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    liked_users = relationship('User', secondary=likes_table, back_populates='liked_posts')
    pub_time = Column(String, default=datetime.utcnow().strftime("%d/%m/%Y %H:%M"))

    def serialize(self):
        return {
            'id': self.id,
            'body': self.body,
            'author_id': self.author_id,
            'liked_users': [user.username for user in self.liked_users],
            'authors_username': session.query(User).filter_by(id=self.author_id).first().username,
            'pub_time': self.pub_time
        }


db.metadata.create_all(engine)
