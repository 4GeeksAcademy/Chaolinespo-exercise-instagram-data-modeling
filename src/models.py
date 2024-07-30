import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

follower_table = Table(
    "follower_table",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("follower_id", ForeignKey("user.id")),
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    follower= relationship("User",secondary="follower_table")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship(User)

    def to_dict(self):
        return {}
    

class Media(Base):
    __tablename__ = 'media'
     # Here we define columns for the table address.
     # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post= relationship(Post)
    type= Column(String(250))
    url= Column(String(250))

    def to_dict(self):
        return {}
    

class Comment(Base):
    __tablename__ = 'comment'
     # Here we define columns for the table address.
     # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    post= relationship(Post)
    author= relationship(User)
    comment_text=Column(String(250))

    def to_dict(self):
        return {}






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

    