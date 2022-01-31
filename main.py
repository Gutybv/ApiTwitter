#Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...,
                           title="User ID")
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., 
                          min_length=8, 
                          max_length=60)

class User(UserBase):    
    first_name: str = Field(...,
                            min_length=2,
                            max_length=50)
    last_name: str = Field(...,
                            min_length=2,
                            max_length=50)
    birthday: date = Field(...)
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(...,
                         max_length=256,
                         min_length=1)
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operations 
@app.get(path="/")
def home():
    return{'Twitter API': 'Working'}

## Users

### Register a user
@app.post(path="/signup",
         response_model=User,
         status_code=status.HTTP_201_CREATED,
         summary='Register a new user',
         tags=['Users'])
def signup():
    pass


### Login a user

@app.post(path="/login",
         response_model=User,
         status_code=status.HTTP_200_OK,
         summary='Login a user',
         tags=['Users'])
def login():
    pass


### Register all users
@app.get(path="/users",
         response_model=List[User],
         status_code=status.HTTP_200_OK,
         summary='Show all users',
         tags=['Users'])
def show_all_users():
    pass

### Register 1 user
@app.get(path="/users/{user_id}",
         response_model=User,
         status_code=status.HTTP_200_OK,
         summary='Register a user',
         tags=['Users'])
def show_a_user():
    pass


### Delete a user
@app.delete(path="/users/{user_id}/delete",
         response_model=User,
         status_code=status.HTTP_200_OK,
         summary='Delete a user',
         tags=['Users'])

def delete_a_user():
    pass

### Update a user
@app.put(path="/users/{user_id}/update",
         response_model=User,
         status_code=status.HTTP_200_OK,
         summary='Update a user',
         tags=['Users'])

def update_a_user():
    pass

#Twitter

### Show all Tweets
@app.post(path="/",
          response_model=List[Tweet],
          status_code=status.HTTP_201_CREATED,
          summary='Show all tweets',
          tags=['Tweets'])
def home():
    pass

### Post a tweet
@app.post(path="/post",
         response_model=Tweet,
         status_code=status.HTTP_201_CREATED,
         summary='Post a Tweet',
         tags=['Tweets'])

def post():
    pass

### Show a tweet
@app.get(path="/tweets/{tweet_id}",
         response_model=Tweet,
         status_code=status.HTTP_200_OK,
         summary='Show a Tweet',
         tags=['Tweets'])

def show_a_tweet():
    pass

### Delete a tweet
@app.delete(path="/tweets/{tweet_id}/delete",
         response_model=Tweet,
         status_code=status.HTTP_200_OK,
         summary='Delete a Tweet',
         tags=['Tweets'])

def delete_a_tweet():
    pass

### Update a tweet
@app.put(path="/tweets/{tweet_id}/update",
         response_model=Tweet,
         status_code=status.HTTP_200_OK,
         summary='Update a Tweet',
         tags=['Tweets'])

def update_a_tweet():
    pass