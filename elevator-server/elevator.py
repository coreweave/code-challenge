from enum import Enum

class State(Enum):
    IDLE = 'idle at'
    UP = 'going up approaching'
    DOWN = 'going down approaching'
    OPEN = 'doors open at'

class Elevator:
    def __init__(self, min_floor: int = -2, max_floor: int = 20):
        self.state = State.IDLE
        self.floor = 1
        self.min_floor = min_floor
        self.max_floor = max_floor

    def __str__(self):
        return 'INFO:      elevator {} floor {}'.format(self.state.value, self.floor)

    def validate(self, floor: int):
        if not (self.min_floor <= floor <= self.max_floor):
            raise ValueError('floor out of range [{}, {}]'.format(self.min_floor, self.max_floor))
    '''
    @param state: the target state
    @return: True if the state transition is legal False otherwise
    '''
    def transition(self, state: State, floor: int):
        if self.state == state:
            self.floor = floor
            return str(self)
        if (self.state == State.IDLE) or ((self.state == State.UP or self.state == State.DOWN) and state == State.OPEN) or (self.state == state.OPEN and state == State.IDLE):
            self.state = state
            return str(self)
        raise ValueError('illegal elevator state transition')

    '''
    @param floor: an integer floor number
    @return: a list of evelator activities
    '''
    async def move(self, floor: int):
        activities = []
        try:
            self.validate(floor)
            activities.append(str(self))
            step = (-1) ** (floor < self.floor)
            state = State.UP if step == 1 else State.DOWN
            for i in range(self.floor, floor + step, step):
                activities.append(self.transition(state, i))
            activities.append(self.transition(State.OPEN, floor))
            activities.append(self.transition(State.IDLE, floor))
        except ValueError as e:
            activities.append('ERROR:      {}'.format(e))
        finally:
            return activities
