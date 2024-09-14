#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, storage_type

if storage_type == 'db':
    from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
    from sqlalchemy.orm import relationship
    from models.review import Review
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if storage_type == 'db':
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', cascade='all, delete',
                                 back_populates='place_amenities',
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter attribute reviews that returns the list of Review instances"""
            from models import storage
            all_reviews = storage.all(Review)
            matched_reviews = []
            for review in all_reviews:
                if self.id == review.place_id:
                    matched_reviews.append(review)
            return matched_reviews

        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity instances"""
            from models.amenity import Amenity
            from models import storage
            all_amenities = storage.all(Amenity)
            matched_amenities = []
            for amenity in all_amenities:
                if amenity.id == self.amenity_ids:
                    matched_amenities.append(amenity)
            return matched_amenities

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids"""
            from models.amenity import Amenity
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
