#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

# fixes the bug
if 'places' in Base.metadata.tables:
    Base.metadata.remove(Base.metadata.tables['places'])

# Defining the place_amenity table for Many-To-Many relationship
place_amenity = Table(
    'place_amenities', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    extend_existing=True  # to allow redefinition
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column("city_id", String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column("user_id", String(60), ForeignKey('users.id'), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024), nullable=True)
    number_rooms = Column("number_rooms", Integer, default=0, nullable=False)
    number_bathrooms = Column("number_bathrooms", Integer, default=0)
    max_guest = Column("max_guest", Integer, default=0, nullable=False)
    price_by_night = Column("price_by_night", Integer, default=0, nullable=False)
    latitude = Column("latitude", Float, nullable=True)
    longitude = Column("longitude", Float, nullable=True)

    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    @property
    def reviews(self):
        """Getter for reviews in FileStorage"""
        from models import storage
        review_instances = storage.all('Review')
        return [review for review in review_instances.values() if review.place_id == self.id]

    @property
    def amenities(self):
        """Getter attr for amenities in FileStorage"""
        from models import storage
        amenity_instances = storage.all('Amenity')
        return [amenity for amenity in amenity_instances.values() if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity_obj):
        from models.amenity import Amenity
        """Setter attr for amenities in FileStorage"""
        if isinstance(amenity_obj, Amenity):
            self.amenity_ids.append(amenity_obj.id)