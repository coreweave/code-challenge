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

    '''
    @param floor: an integer floor number
    @return: None, raises ValueError is floor is out of range
    '''
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
    @param target_floor: an integer floor number
    @return: a list of evelator activities
    '''
    async def move(self, target_floor: int):
        activities = []
        try:
            self.validate(target_floor)
            activities.append(str(self))
            step = (-1) ** (target_floor < self.floor)
            state = State.UP if step == 1 else State.DOWN
            for floor in range(self.floor, target_floor + step, step):
                activities.append(self.transition(state, floor))
            activities.append(self.transition(State.OPEN, target_floor))
            activities.append(self.transition(State.IDLE, target_floor))
        except ValueError as e:
            activities.append('ERROR:      {}'.format(e))
        finally:
            return activities
