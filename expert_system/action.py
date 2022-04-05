"""
Move
"""
from simulator.case import Case


class Action:
    description = ''  # MOVE, FIRE, RUBBLE, SURVIVOR
    direction = ''  # UP,DOWN,LEFT,RIGHT
    destination_case = None

    def __init__(self, description: str, destination_case: Case) -> None:
        self.description = description
        self.destination_case = destination_case

    def set_current_position(self, x, y) -> None:
        if self.destination_case.x > x:
            self.direction = 'RIGHT'
        if self.destination_case.x < x:
            self.direction = 'LEFT'
        if self.destination_case.y > y:
            self.direction = 'DOWN'
        if self.destination_case.y < y:
            self.direction = 'UP'
