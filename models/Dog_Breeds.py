from codecs import backslashreplace_errors
from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table

class Dog_Breeds(Base):
    __tablename__ = "dogs_breeds"
    dog_id = Column(ForeignKey("dogs.id"),primary_key=True)
    breed_id = Column(ForeignKey("breeds.id"),primary_key=True)
    dogs = relationship("Dog", back_populates="breeds")
    breeds = relationship("Breed", back_populates="dogs")