from pydantic import BaseModel,EmailStr

class Users(BaseModel):
    id:int
    username:str
    email:str
    password:str
    class Config:
        orm_mode = True


