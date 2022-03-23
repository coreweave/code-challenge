# from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class State(Enum):
    IDLE = 1
    UP = 2
    DOWN = 3
    DOORSOPEN = 4

class Elevator:
    floor : int
    state: State

    def move(self, target):

'''
@param floor_number: clients can submit a desired floor number for the elevator to move to
@return: None. The server should determine where the elevator should move next and print a log of evelator activities and decisions or elevator state.
'''
@app.post('/floor/{floor_number}')
async def moveElevator(floor_number: int):
    print('ELEVATOR:     at floor {} - state {} - going}')
    return {'floor_number': floor_number}