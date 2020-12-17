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
from os import getenv

classes = {
    'State': State,
    'City': City,
    'Place': Place,
    'Amenity': Amenity,
    'Review': Review,
    'User': User
}


class DBStorage:
    """This class manages storage of hbnb models in SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        environment = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database), pool_pre_ping=True)
        if environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all the database storage"""
        queryList = []
        queryDict = {}
        if cls in classes:
            obj = self.__session.query(classes[cls]).all()
            for obj_ in obj:
                key = "{}.{}".format(obj_.__class__.__name__, obj_.id)
                value = obj_
                queryDict[key] = value
        elif cls is None:
            for cls_ in classes:
                obj = self.__session.query(classes[cls]).all()
                for obj_ in obj:
                    key = "{}.{}".format(obj_.__class__.__name__, obj_.id)
                    value = obj_
                    queryDict[key] = value
        return queryDict

    def new(self, obj):
        """Add object to the current database"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """save all changes to current session in database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete changes from the current session to database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and current database session"""
        Base.metadata.create_all(self.__engine)
        Session_ = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_)
        self.__session = Session()
