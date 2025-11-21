from fastapi import FastAPI,Body
app=FastAPI()
@app.post("/add_user")
def add_user(name: str = Body(...), age: int = Body(...)):
    return {"message": f"User {name} aged {age} added successfully"}
