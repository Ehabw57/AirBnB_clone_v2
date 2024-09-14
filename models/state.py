#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_type


class State(BaseModel, Base):
    """ State class """
    name = ""

    if storage_type == 'db':
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """Getter attribute cities
            that returns the list of City instances"""
            from models import storage
            from models.city import City
            all = storage.all(City)
            city_list = []
            for city in all.values():
                if city.__dict__.get('state_id') == self.id:
                    city_list.append(city)
            return city_list
