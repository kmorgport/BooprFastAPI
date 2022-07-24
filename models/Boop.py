from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
import models.User

class Boop(Base):
    __tablename__ = "boops"
    id = Column(Integer, primary_key=True, nullable=False)
    # #ManyToOne
    image_id = Column(Integer, ForeignKey("images.id", ondelete="CASCADE"), nullable=False)
    image = relationship("Image", back_populates="boops")
    # #ManyToOne = 
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="boops")
    