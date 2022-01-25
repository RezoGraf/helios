# app.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random
import uvicorn
from routers import report
from typing import List

app = FastAPI()
app.include_router(user.router)

class User(BaseModel):
    name: str
    age: int
    
class Metadata(BaseModel):
    series: List[str]

{
  "series": ["GOT", "Dark", "Mr. Robot"]
}

class UserGroup(BaseModel):
    users: List[User]
    group: str
    
{
  "users": [
    {
      "name": "xyz",
      "age": 25
    },
    {
      "name": "abc",
      "age": 30
    }
  ],
  "group": "Group A"
}

@app.post('/users')
def save_user(user: User):
    return {'name': user.name,
            'age': user.age}
    
    
@app.get("/", response_class=PlainTextResponse)
async def hello():
    return "Hello World!"