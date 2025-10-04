from fastapi import APIRouter
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/todos", tags=["CRUD"])

todos = [1, 2, 3, 4]


@router.post("/")
async def create_todo():
    todos.append(len(todos))
    return todos[-1]


@router.get("/")
async def get_todos():
    return todos


@router.get("/{id}")
async def get_todo_by_id(id: int):
    try:
        res = todos[id]
        return res
    except:
        return HTTPException(status_code=404, detail="Todo not found")


@router.put("/{id}")
async def update_todo_by_id(id: int, new_todo: int):
    try:
        todos[id] = new_todo
        return new_todo
    except:
        return HTTPException(status_code=404, detail="Todo not found")


@router.delete("/{id}")
async def delete_todo_by_id(id: int):
    try:
        del todos[id]
        return {"msg": "ok"}
    except:
        return HTTPException(status_code=404, detail="Todo not found")
