from contextlib import nullcontext
from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Dog(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    sex = Column(Boolean, nullable=False)
    bio = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
