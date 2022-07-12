from contextlib import nullcontext
from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
# from .joinTables import breed_table

class Dog(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    sex = Column(Boolean, nullable=False)
    bio = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    # ManyToMany
    # breeds = relationship(
    #     #String matches Class Name
    #     #back_populates matches field name in joined class
    #     "Breed", secondary=breed_table, back_populates="dogs"
    # )
    # OneToMany
    images = relationship("Image", back_populates="dog")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("Users", back_populates="dogs")