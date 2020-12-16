#!/usr/bin/python3
""" New engine for HBNB project """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in SQLAlchemy"""
    pass

