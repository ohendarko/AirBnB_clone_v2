#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, CHAR
from datetime import datetime


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""
    id = Column("id", String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column("created_at", nullable=False, default=datetime.utcnow())
    updated_at = Column("updated_at", nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            # initialize from scratch
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        else: #if key, value pair present
            for key, value in kwargs.items():
                if key not in ['__class__', 'created_at', 'updated_at']:
                    setattr(self, key, value) # create instance attributes from the dictionary.

                #  If 'created_at' or 'updated_at' is present in kwargs, it converts the
                #  string representation of the datetime to a datetime object using strptime
                # Chat's idea
                if 'updated_at' in kwargs:
                    if isinstance(kwargs['updated_at'], str):
                        kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                                 '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        # No need to convert if it's already a datetime object
                        pass
                if 'created_at' in kwargs:
                    if isinstance(kwargs['created_at'], str):
                        kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                                 '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        # No need to convert if it's already a datetime object
                        pass
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        if '_sa_instance_state' in dictionary:
            # If the '_sa_instance_state' key is present in the dictionary
            # (which is added by SQLAlchemy for its internal use), it is removed.
            del dictionary['_sa_instance_state']
            # This ensures that only the user-defined attributes
            # are included in the dictionary
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
        storage.save()