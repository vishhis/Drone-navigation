
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Follow-Me Drone API 🚀")

# Define a command input model
class Command(BaseModel):
    direction: str

@app.get("/")
async def root():
    return {"message": "Follow-Me Drone API is up and running!"}

@app.post("/move-drone/")
async def move_drone(command: Command):
    direction = command.direction.lower()
    if direction in ["up", "down", "left", "right", "forward", "backward"]:
        # Simulate drone behavior
        return {"status": "success", "action": f"Drone is moving {direction}"}
    else:
        return {"status": "error", "message": "Invalid direction. Please use up, down, left, right, forward, or backward."}
