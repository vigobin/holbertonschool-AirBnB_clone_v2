#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete',
                          back_populates='state')

    @property
    def cities(self):
        """Getter class for City attributes"""
        city_list = []
        get_cities = models.storage.all(City)
        for i in get_cities.values():
            if i.state_id == self.id:
                city_list.append(i)
        return city_list
