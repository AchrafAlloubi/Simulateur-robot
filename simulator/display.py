"""
Affichage
"""
from simulator.environment import Environment
from tweak import Tweak


class Display:

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

    def print_map(self, environment: Environment):
        """
        Affichage de la matrice
        """
        if Tweak().debug:
            print('------MAP-------')
        for y in range(len(environment.matrix)):
            line = ''
            for x in range(len(environment.matrix[y])):
                case = environment.get_case(x, y)
                line += case.display() + ' '
            print(line)
