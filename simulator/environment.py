"""
Légende: Data Environnement
__ Case Vide
1-Case Poussière
2-Case Bijou
3-Case Poussière+Bijou
10-Case Joueur
"""

from simulator.case import Case
from tweak import Tweak


class Environment:
    length_x = None
    length_y = None
    matrix = []
    robot_position_y = None
    robot_position_x = None

    def __call__(self) -> None:
        return

    def __init__(self, length_x, length_y) -> None:
        self.length_x = length_x
        self.length_y = length_y
        self.create_matrix()
        return

    def create_matrix(self):
        self.matrix = []
        for y in range(self.length_y):
            self.matrix.append([])
            for x in range(self.length_x):
                case = Case(x, y)
                self.matrix[y].append(case)

    def get_adjacent_cases(self, x, y) -> []:
        all_case = []
        if x > 0:
            all_case.append(self.get_case(x - 1, y))
        if x < self.length_x - 1:
            all_case.append(self.get_case(x + 1, y))
        if y > 0:
            all_case.append(self.get_case(x, y - 1))
        if y < self.length_y - 1:
            all_case.append(self.get_case(x, y + 1))
        return all_case

    def get_case(self, x, y) -> Case:
        return self.matrix[y][x]

    def set_robot_position(self, x, y):
        print_position = '(' + str(x) + ',' + str(y) + ')'
        if Tweak().debug:
            print('Agent', print_position)
        self.robot_position_x = x
        self.robot_position_y = y
        case = self.get_case(x, y)
        case.set_robot(True)