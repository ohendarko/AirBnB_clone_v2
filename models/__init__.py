#!/usr/bin/python3
"""
a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
If equal to db:
    Import DBStorage class in this file
    Create an instance of DBStorage and store it in the variable storage
    (the line storage.reload() should be executed after this instantiation)
Else:
    Import FileStorage class in this file
    Create an instance of FileStorage and store it in the variable storage
    (the line storage.reload() should be executed after this instantiation)
"""
from models.engine.file_storage import FileStorage
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    storage = FileStorage()

storage.reload()
