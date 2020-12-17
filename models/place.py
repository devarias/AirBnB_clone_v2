#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place')
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """to list all the reviews"""
            from models import storage
            reviewsList = []
            for key, obj in storage.all(Review).items():
                if self.id == obj.place_id:
                    reviewsList.append(obj)
            return reviewsList

        @property
        def amenities(self):
            """getter to list all the amenities"""
            from models import storage
            from models.amenity import Amenity
            amenityList = []
            for key, obj in storage.all(Amenity).items():
                if self.id == obj.amenity_ids:
                    amenityList.append(obj)
            return amenityList

        @amenities.setter
        def amenities(self, amenit):
            """setter to list all the amenities"""
            from models.amenity import Amenity
            if type(amenit) == Amenity:
                    self.append(amenit)
