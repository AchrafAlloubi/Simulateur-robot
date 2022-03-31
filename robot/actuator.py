"""
Interraction de du robot avec
"""
from communication.environment_controller import EnvironmentController


class Actuator:
    environment_controller = EnvironmentController()

    def __call__(self) -> None:
        return

    def __init__(self):

        return

    def move_left(self):
        self.environment_controller.environment.robot_position_x -= 1

    def move_right(self):
        self.environment_controller.environment.robot_position_x += 1

    def move_up(self):
        self.environment_controller.environment.robot_position_y -= 1

    def move_down(self):
        self.environment_controller.environment.robot_position_y += 1

    def aspire(self, x, y):
        # Enlève tout ce qui est sur cette case
        # self.environment_controller.environment.matrix[y][x] = 0
        print("Aspire !!!!!!!!")
        self.environment_controller.clear_piece(x, y)

    def collect(self, x, y):
        # Enlève tout ce qui est sur cette case
        # self.environment_controller.environment.matrix[y][x] = 0
        print("Collect !!!!!!!")
        self.environment_controller.clear_piece(x, y)
