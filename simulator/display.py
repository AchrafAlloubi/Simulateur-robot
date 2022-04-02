"""
Affichage
"""
from robot.robot import Robot
from tweak import Tweak


class Display:

    def __call__(self) -> None:
        return

    def print_main_title(self):
        print('TP3 - Agent logique')
        print('le simulateur de robot sauve des vies')
        print('')

    def print_legend(self):
        print('A - agent, F - feu, C - chauffer')
        print('P - poussière, D - décombres, G - gens')
        print('')

    def print_level_title(self, level, length):
        print('Tableau niveau ', level, ' - ', length, 'x', length)

    def print_map(self, environment):
        """
        Affichage de la matrice
        """
        #todo adapter ça
        #matrix = self.environment_controller.environment.get_matrix()
        if Tweak().debug:
            print('------MAP-------')
        for y in range(len(environment.matrix)):
            line = ''
            for x in range(len(environment.matrix[y])):
                case = environment.get_slot_data(x, y)
                line += case.display()+' '
            print(line)

        #print('------TEST EXPLORATION-------')
        #print(str(self.environment_controller.environment.test_exploration()))

        # self.print_metric()

        # self.print_state()

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
