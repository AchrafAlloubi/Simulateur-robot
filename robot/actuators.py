"""
Interraction du robot avec l'environnement
"""
from simulator.environment import Environment


class Actuators:

    def __call__(self) -> None:
        return

    def __init__(self):
        return

    def move_left(self, global_environment: Environment):
        global_environment.robot_position_x -= 1

    def move_right(self, global_environment: Environment):
        global_environment.robot_position_x += 1

    def move_up(self, global_environment: Environment):
        global_environment.robot_position_y -= 1

    def move_down(self, global_environment: Environment):
        global_environment.robot_position_y += 1

    def use_extinguisher(self, global_environment: Environment, target_x: int, target_y: int):
        # TODO Utiliser son extincteur pour jeter de l'eau et éteindre le feu
        return

    def aspire(self, x, y):
        # Enlève tout ce qui est sur cette case
        # self.global_environment.matrix[y][x] = 0
        print("Aspire !!!!!!!!")
        self.environment_controller.clear_piece(x, y)

    def collect(self, x, y):
        # Enlève tout ce qui est sur cette case
        # self.global_environment.matrix[y][x] = 0
        print("Collect !!!!!!!")
        self.environment_controller.clear_piece(x, y)
