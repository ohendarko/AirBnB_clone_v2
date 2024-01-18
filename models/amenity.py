#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

place_amenity_association = Table(
    'place_amenities', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)


class Amenity(BaseModel, Base):
    name = Column("name", String(128), nullable=False)

    place_amenities = relationship('Place', secondary=place_amenity_association, back_populates='amenities')