from typing import List

from fastapi import FastAPI, HTTPException
from models import User_Pydantic, UserIn_Pydantic, Users
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title="Tortoise ORM FastAPI example")


class Status(BaseModel):
    message: str



@app.post("/usersPucem", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)



register_tortoise(
    app,
    db_url="postgres://postgres:6541@172.21.166.235:5433/examen_orm",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)