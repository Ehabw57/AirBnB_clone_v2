from models.base_model import BaseModel, Base, storage_type


class Amenity(BaseModel, Base):
    """ Amenity class for storing amenity information """
    name = ""

    if storage_type == 'db':
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        from models.place import place_amenity
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")
