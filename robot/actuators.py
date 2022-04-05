"""
Interraction du robot avec l'environnement
"""
import random

from simulator.case import Case
from simulator.environment import Environment
from tweak import Tweak


class Actuators:
    environment: Environment = None
    current_case: Case = None

    def __init__(self, global_environment: Environment) -> None:
        self.environment = global_environment
        self.current_case = self.environment.get_case(self.environment.robot_position_x,
                                                      self.environment.robot_position_y)

    def move_left(self):
        self.get_current_case().set_robot(False)
        self.environment.robot_position_x -= 1
        self.get_current_case().set_robot(True)

    def move_right(self):
        self.get_current_case().set_robot(False)
        self.environment.robot_position_x += 1
        self.get_current_case().set_robot(True)

    def move_up(self):
        self.get_current_case().set_robot(False)
        self.environment.robot_position_y -= 1
        self.get_current_case().set_robot(True)

    def move_down(self):
        self.get_current_case().set_robot(False)
        self.environment.robot_position_y += 1
        self.get_current_case().set_robot(True)

    def use_extinguisher(self, target_case):
        # Utilise son extincteur pour jeter de l'eau et éteindre le feu
        target_case.set_fire(False)
        hot_cases = self.environment.get_adjacent_cases(target_case.x, target_case.y)
        for case in hot_cases:
            case.is_hot = False
        return

    def identify_rubble(self) -> bool:
        # Lors de la détection de décombres, vous devez esquiver pour ne pas rester coincé
        # 30% de chance de mourrir
        percent = random.randrange(0, 100)
        return percent > Tweak.trapped_rate

    def get_current_case(self):
        return self.environment.get_case(self.environment.robot_position_x,
                                         self.environment.robot_position_y)
