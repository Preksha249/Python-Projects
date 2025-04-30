from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    # User is a table here and below are the columns. Columns data types are defined. 
    # Attributes defined
    id: Optional[UUID] = uuid4() #Universallu unique identifier. 
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    roles: Optional[List[Role]] = None