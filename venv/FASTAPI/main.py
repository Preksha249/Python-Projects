from typing import Union, List
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
         id=UUID("689e2eb3-687c-4c9a-b547-0cef8e94a5d5"), 
         first_name = "Jamila",
         last_name="bleh",
         gender=Gender.female,
         roles = [Role.student]
    ),
    User(
         id=UUID("d3c43778-7d34-4e53-bcec-c2e8cb7b2ac2"), 
         first_name = "Alex",
         last_name="Jon",
         gender=Gender.male,
         roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, 
        detail=f"user with id: {user_id} does not exist"
    )