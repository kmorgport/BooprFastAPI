from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
breed_table = Table(
    "dogs_breeds",
    Base.metadata,
    Column("dog_id", ForeignKey("dogs.id"), primary_key=True),
    Column("breed_id", ForeignKey("breeds.id"), primary_key=True)
)