from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from .joinTables import breed_table
import models.Dog

class Breed(Base):
    __tablename__ = "breeds"
    id = Column(Integer, primary_key=True, nullable=False)
    breed = Column(String, nullable=False)
    dogs = relationship(
        #String matches Class Name
        #back_populates matches field name in joined class
        "Dog", secondary=breed_table, back_populates="breeds"
    )
