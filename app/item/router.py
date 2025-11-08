from fastapi import APIRouter

from app.core import Database
import app.item.repo as Repository

router = APIRouter()

@router.get("/items")
async def get_items(db: Database):
    return Repository.read_all(db)
    
