#!/usr/bin/python3
"""DOC pending"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os


class DBStorage:
    """pending"""
    __engine = None
    __session = None

    def __init__(self):
        """pending"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        hostname = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.environ.get('HBNB_ENV')

        connection_string = f'mysql+mysqldb://{user}:{password}@{hostname}/{database}?charset=utf8'

        """if env == 'test':
            # adjusts the connection_string based on
            # whether the environment is set to 'test' or not.
            connection_string += '&hostname=localhost&port=3306&charset=utf8'
        else:
            connection_string += '&pool_pre_ping=True'
        """
        self.__engine = create_engine(connection_string, pool_pre_ping=True)
        if env == 'test':
            # drop all tables if the environment variable
            # HBNB_ENV is equal to test
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        objects = []
        query_classes = []

        if cls:
            # if cls specified, use in query
            if isinstance(cls, str):
                query_class = globals().get(cls, None)
                if query_classes:
                    query_classes.append(query_class)
            else:
                query_classes.append(cls)
        else:
            # If cls is None, query all types of objects
            query_classes = [User, State, City, Amenity, Place, Review]

        for query_class in query_classes:
            for obj in self.__session.query(query_class):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """add the object to the current database session
        (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and
        create the current database session."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)