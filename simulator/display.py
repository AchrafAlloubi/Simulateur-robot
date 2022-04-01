"""
Affichage
"""
from communication.environment_controller import EnvironmentController
from robot.robot import Robot
from simulator.simulator import Tweak


class Display:
    environment_controller = EnvironmentController()
    metric = Robot().believe.metric
    state = Robot().believe.state

    def __call__(self) -> None:
        self.environment_controller = EnvironmentController()
        return

    def print_title(self):
        print('TP3 - Agent logique')
        print('le simulateur de robot sauve des vies')

    def print_legend(self):
        print('A - agent, F - feu, C - chauffer')
        print('P - poussière, D - décombres, G - gens')

    def print_map(self):
        """
        Affichage de la matrice
        """
        matrix = self.environment_controller.environment.get_matrix()
        if Tweak().debug:
            print('------MAP-------')
        for y in range(len(matrix)-1, -1, -1):
            print(matrix[y])

        #print('------TEST EXPLORATION-------')
        #print(str(self.environment_controller.environment.test_exploration()))

        self.print_metric()

        self.print_state()

        # TODO Terminé
        # self.environment_controller.need_screen_refresh = False

    def print_metric(self) -> None:
        if Tweak().debug:
            print('-----METRIC-----')
            print(vars(self.metric))

    def print_state(self) -> None:
        if Tweak().debug:
            print('-----STATE-----')
            print(vars(self.state))
