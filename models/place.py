#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
import models

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
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
    amenity_ids = []

    type_storage = getenv("HBNB_TYPE_STORAGE")
    if type_storage == "db":
        reviews = relationship('Review', cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            new_list = []
            revi = storage.all(Review).values()
            for i in revi:
                if i.place_id == self.id:
                    new_list.append(i)
            return new_list

        @property
        def amenities(self):
            """Amenity getter"""
            from models.amenity import Amenity
            from models import storage
            amenity_list = []
            ameni = storage.all(Amenity).values()
            for i in ameni:
                if i.place_id == self.id:
                    amenity_list.append(i)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity_list):
            """Amenity setter"""
            from models.amenity import Amenity
            for i in amenity_list:
                if type(i) == Amenity:
                    self.amenity_ids.append(i)
