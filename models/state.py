#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, CHAR, ForeignKey, create_engine
from sqlalchemy.orm import relationship

# fixes the bug
if 'states' in Base.metadata.tables:
    Base.metadata.remove(Base.metadata.tables['states'])



class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)

    # For DBStorage; cities must represent a relationship with the class City
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    # For FileStorage; getter attribute cities that returns the list of City instances
    # with state_id equals to the current
    @property
    def cities(self):
        """getter attribute for cities in FileStorage"""
        from models import storage
        city_instances = storage.all('City')
        return [city for city in city_instances.values() if city.state_id == self.id]