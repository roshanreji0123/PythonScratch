from fastapi import FastAPI
app=FastAPI()
@app.get("/home") # route is /home 
                 # decorator is a function that 
                 #modifies the behavior of another function
                 
def home():
    return {"message": "Hello Roshan!"}

@app.get("/")# route is /
def home_function():
    return {"message":"Im learning FASTAPI"}

#query parameters 
@app.get("/multiply")
def multiply(a:int,b:int):
    return{"PRODUCT":a*b} # http://127.0.0.1:8000/multiply?a=5&b=4 url 
                            # gives {"PRODUCT":20} as output on browser