from fastapi import FastAPI
from elevator import Elevator

app = FastAPI()
elevator = Elevator()

@app.post('/floor/{floor}')
async def moveElevator(floor: int):
    activities = await elevator.move(floor)
    return {'activities': activities}