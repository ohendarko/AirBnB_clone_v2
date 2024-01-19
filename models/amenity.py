#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

# fixes the bug
if "amenities" in Base.metadata.tables:
    Base.metadata.remove(Base.metadata.tables["amenities"])


# # Defining the association table for the Many-to-Many relationship
place_amenity = Table(
    'place_amenities', Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60),
           ForeignKey('amenities.id'), primary_key=True, nullable=False),
    extend_existing=True  # to allow redefinition
)


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column("name", String(128), nullable=False)

    # class attribute place_amenities must represent a relationship
    # Many-To-Many between the class Place and Amenity.
    place_amenities = relationship('Place', secondary=place_amenity,
                                   viewonly=False)
