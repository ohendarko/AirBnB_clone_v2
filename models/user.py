#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

# fixes the bug
if 'users' in Base.metadata.tables:
    Base.metadata.remove(Base.metadata.tables.get('users'))

user_review_association = Table(
    'user_reviews', Base.metadata,
    Column('user_id', String(60),
           ForeignKey('users.id'), primary_key=True, nullable=False),
    Column('review_id', String(60),
           ForeignKey('reviews.id'), primary_key=True, nullable=False),
    extend_existing=True  # To allow redefinition
)


class User(BaseModel, Base):
    """Defines a user by various attributes for mySQL db
    Inherits from SQLAlchemy's Base and links to a table called user.
    Attributes:
    __tablename__ (str): The name of the MySQL table to store users.
    email: (sqlalchemy String): User email address.
    password (sqlalchemy String): User password.
    first_name (sqlalchemy String): User first name.
    last_name (sqlalchemy String): User last name.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user',
                          cascade='all, delete-orphan')
    reviews = relationship('Review', backref='user',
                           cascade='all, delete-orphan')
