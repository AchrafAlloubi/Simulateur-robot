"""
Représence ce que le robot voit
"""
from communication.environment_controller import EnvironmentController
from simulator.simulator import Environment


class Sensor:
    environment_controller = EnvironmentController()

    def __call__(self) -> None:
        return

    def __init__(self, ) -> None:
        return

    def get_environment(self) -> Environment:
        return self.environment_controller.environment

    def detect_heat(self):
        # Todo Retourner les cases qui contiennent de la chaleur
        return

    def detect_heat(self, case):
        # Todo Vérifier si la case contient du feu
        return

    def detect_dust(self):
        # Todo Retourner les cases qui contiennent de la poussière
        return

    def identify_rubble(self):
        # Todo Lors de la détection de décombres, vous devez esquiver pour ne pas rester coincé
        return

    def use_microphone(self):
        # Todo Détecter les cris
        return

    def get_dust_and_jewel(self) -> []:
        # TODO NE REST PLUS : Ça vient du tp1
        matrix = self.environment_controller.environment.get_matrix()
        object_found = []

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] in (1, 2, 3):
                    object_found.append([x, y])
        nb = str(len(object_found))
        #print("Objet found:"+nb)
        return object_found
