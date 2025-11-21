from fastapi import FastAPI, Body, HTTPException

app = FastAPI()
users = {}

# CREATE
@app.post("/users")
def add_user(name: str = Body(...), age: int = Body(...)):
    user_id = len(users) + 1
    users[user_id] = {"name": name, "age": age}
    return {"id": user_id, "user": users[user_id]}

# READ ALL
@app.get("/users")
def get_users():
    return users

# READ ONE
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# UPDATE (FULL - PUT)
@app.put("/users/{user_id}")
def rewrite_user(user_id: int, name: str = Body(...), age: int = Body(...)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    users[user_id] = {"name": name, "age": age}
    return {"message": "User updated successfully", "user": users[user_id]}

# UPDATE (PARTIAL - PATCH)
@app.patch("/users/{user_id}")
def update_user(user_id: int, name: str | None = Body(None), age: int | None = Body(None)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        users[user_id]["name"] = name
    if age is not None:
        users[user_id]["age"] = age

    return {"message": "User partially updated", "user": users[user_id]}

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    deleted = users.pop(user_id)
    return {"message": "User deleted", "user": deleted}
