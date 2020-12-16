#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=Flase)
    cities = relationship("City", backref='states')

    @property
    def cities(self):
        """to list the cities"""
        from models import storage
        if os.getenv(HBNB_TYPE_STORAGE) != 'db':
            citiesList = []
            for key in storage.all(City).items():
                for key2 in storage.all(State).items():
                    if key.id == key2.id:
                        citiesList.append(id1)
        return citiesList
