from uuid import UUID
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    done: bool


class TodoShow(Todo):
    id: UUID
    user_id: UUID
