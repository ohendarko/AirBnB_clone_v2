#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column("state_id", String(60), ForeignKey('states.id'), nullable=False)
    name = Column("name", String(128), nullable=False)

    # places must represent a relationship with the class Place...
    places = relationship('Place', backref='city', cascade='all, delete-orphan')