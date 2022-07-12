from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

class ImageBase(BaseModel):
    url: str