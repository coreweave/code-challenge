from enum import Enum

class State(Enum):
    IDLE = 'idle'
    UP = 'going up'
    DOWN = 'going down'
    DOORSOPEN = 'doors open'

class Elevator:
    def __init__(self, min_floor = -2, max_floor = 20):
        self.floor = 1
        self.state = State.IDLE
        self.min_floor = min_floor
        self.max_floor = max_floor

    '''
    @param target_floor: Clients can submit a desired floor number for the elevator to move to.
    @return: None. The server should determine where the elevator should move next and print a log of evelator activities.
    '''
    async def move(self, target_floor):
        activities = []
        if not (self.min_floor <= target_floor <= self.max_floor):
            activities.append('ERROR:      target floor is out of range - valid range [{}, {}]'.format(self.min_floor, self.max_floor))
            return activities
        
        activities.append('LOG:      elevator at floor {} - {}'.format(self.floor, self.state))
        step = 1 if target_floor >= self.floor else -1
        self.state = State.UP if step == 1 else State.DOWN
        for i in range(self.floor, target_floor + 1, step):
            self.floor = i
            activities.append('LOG:      elevator {} - approaching {}'.format(self.state, self.floor))
        self.state = State.DOORSOPEN
        activities.append('LOG:      elevator at floor {} - {}'.format(self.floor, self.state))
        self.state = State.IDLE
        return activities
