#Python
from uuid import UUID
from datetime import date
from typing import Optional
#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI

app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...,
                           title="User ID")
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., 
                          min_length=8, 
                          max_length=20)

class User(UserBase):    
    first_name: str = Field(...,
                            min_length=2,
                            max_length=50)
    last_name: str = Field(...,
                            min_length=2,
                            max_length=50)
    birthday: date = Field(...)



class Tweet(BaseModel):
    pass


@app.get(path="/")
def home():
    return{'Twitter API': 'Working'}