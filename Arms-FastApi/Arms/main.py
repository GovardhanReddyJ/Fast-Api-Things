from fastapi import APIRouter, Depends,FastAPI
from sqlalchemy.orm import Session
from typing import List
from dependencies.database import get_db
from schemas.item import Users 
app = FastAPI()

router = APIRouter()

@router.get("/users", response_model=List[Users])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users 


