"""
Représence ce que le robot voit
"""
from communication.environment_controller import EnvironmentController
from simulator.environment import Environment


class Sensor:
    environment_controller = EnvironmentController()

    def __call__(self) -> None:
        return

    def __init__(self, ) -> None:
        return

    def get_environment(self) -> Environment:
        return self.environment_controller.environment

    def get_dust_and_jewel(self) -> []:
        matrix = self.environment_controller.environment.get_matrix()
        object_found = []

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] in (1, 2, 3):
                    object_found.append([x, y])
        nb = str(len(object_found))
        #print("Objet found:"+nb)
        return object_found
