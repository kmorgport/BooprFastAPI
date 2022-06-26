from datetime import datetime
from distutils.util import strtobool
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None