#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state')
    else:
        @property
        def cities(self):
            """to list the cities"""
            from models import storage
            citiesList = []
            for key, obj in storage.all(City).items():
                if self.id == obj.state_id:
                    citiesList.append(obj)
            return citiesList
