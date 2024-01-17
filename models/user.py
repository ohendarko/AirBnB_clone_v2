#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

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
    __table__name = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
