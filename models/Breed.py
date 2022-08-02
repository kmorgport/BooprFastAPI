from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
import models.Dog

class Breed(Base):
    __tablename__ = "breeds"
    id = Column(Integer, primary_key=True, nullable=False)
    breed = Column(String, nullable=False)
    dogs = relationship("Dog_Breeds", back_populates="breeds")
