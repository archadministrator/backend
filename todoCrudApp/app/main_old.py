from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
 
app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

todos = []

@app.get("/")
def readRoot():
    return {"message": "Hello sir, todo app is running good"}

@app.get("/todos")
def getTodos():
    return todos

@app.get("/todos/{todoId}")
def getTodo(todoId: int):
    for todo in todos:
        if todo.id == todoId:
            return todo
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/todos")
def createTodo(todo: Todo):
    todos.append(todo)
    return todo

@app.put("/todos/{todoId}")
def updateTodo(todoId: int, updatedTodo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todoId:
            todos[i] = updatedTodo
            return updatedTodo
    raise HTTPException(status_code=404, detail="Task not found!")

@app.delete("/todos/{todoId}")
def deleteTodo(todoId: int):
    for i, todo in enumerate(todos):
        if todo.id == todoId:
            todos.pop(i)
            return {"message": "Task deleted!"}
    raise HTTPException(status_code=404, detail="Task not found")

# Bước tiếp theo: tạo database, model, crud sử dụng SQLAlchemy > Auth + User Perm > Deploy > Buld Frontend.