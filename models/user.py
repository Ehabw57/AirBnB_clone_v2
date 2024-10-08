#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, storage_type


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    if storage_type == 'db':
        __tablename__ = "users"
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', back_populates='user',
                              cascade="all, delete")
        reviews = relationship('Review', back_populates='user',
                               cascade="all, delete")
