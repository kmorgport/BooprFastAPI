from contextlib import nullcontext
from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
import models.Dog
import models.User

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String, nullable=False)
    #OneToMany
    boops = relationship("Boop", back_populates="image")
    #ManyToOne
    dog_id = Column(Integer, ForeignKey("dogs.id", ondelete="CASCADE"), nullable=False)
    dog = relationship("Dog", back_populates="images")
    #ManyToOne
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="images")