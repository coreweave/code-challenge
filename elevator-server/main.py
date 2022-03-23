from fastapi import FastAPI
from elevator import Elevator

app = FastAPI()
elevator = Elevator()

@app.post('/floor/{target_floor}')
async def moveElevator(target_floor: int):
    activities = await elevator.move(target_floor)
    return {'activities': activities}