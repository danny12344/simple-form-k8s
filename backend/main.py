import sys
from loguru import logger

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

logger.add(
    sink=sys.stdout,  # Output logs to the console
    format="{time} {level} {message}",
    level="ERROR"
)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to limit access to specific origins
    allow_methods=["*"],
    allow_headers=["*"],
)

username = ""
password = ""

@app.post("/submit")
async def submit_form_data(request: Request):
    form_data = await request.json()
    print(form_data)
    logger.info(form_data)
    username = form_data.get("username")
    password = form_data.get("password")
    
    return {"message": "Data submitted successfully"}

@app.get("/data")
async def get_data():
    global username, password
    return {"username": username, "password": password}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
