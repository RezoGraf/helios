# routers/report.py
from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

@router.get('/users')
def list_users():
    return {'users': ['a', 'b', 'c']}