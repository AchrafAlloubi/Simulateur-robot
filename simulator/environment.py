"""
Légende: Data Environnement
__ Case Vide
1-Case Poussière
2-Case Bijou
3-Case Poussière+Bijou
10-Case Joueur
"""

from exploration.informed import Informed
from exploration.uninformed import Uninformed
from simulator.case import Case


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
            all_case.append(self.get_slot_data(x - 1, y))
        if x < self.length_x - 1:
            all_case.append(self.get_slot_data(x + 1, y))
        if y > 0:
            all_case.append(self.get_slot_data(x, y - 1))
        if y < self.length_y - 1:
            all_case.append(self.get_slot_data(x, y + 1))
        return all_case

    def get_matrix(self) -> []:
        return self.matrix
        # Copie de la matrice
        matrix = []
        for y in range(len(self.matrix)):
            matrix.append([])
            for x in range(len(self.matrix[y])):
                matrix[y].append(self.matrix[y][x])

        return matrix

    def contained_matrix(self, pos_x, pos_y, matrix):
        if pos_y >= len(matrix) or pos_y < 0:
            return False
        if pos_x >= len(matrix[len(matrix) - 1]) or pos_x < 0:
            return False
        return True

    def get_slot_data(self, x, y) -> Case:
        return self.matrix[y][x]

    def add_slot_data(self, x, y, data_id):
        """
        Ne sert plus
        case = self.matrix[y][x]
        if data_id == 2:  # Is Jewel
            if slot_id == 1:
                self.matrix[y][x] = 3  # New Status = Both Jewel and Dust
            elif slot_id != 3:
                self.matrix[y][x] = data_id
        elif data_id == 1:  # Is Dust
            if slot_id == 2:
                self.matrix[y][x] = 3
            elif slot_id != 3:
                self.matrix[y][x] = data_id
        """
        return


    def get_size_x(self):
        return self.length_x

    def get_size_y(self):
        return self.length_y

    def set_robot_position(self, x, y):
        print_position = '(' + str(x) + ',' + str(y) + ')'
        print('Agent', print_position)
        self.robot_position_x = x
        self.robot_position_y = y
        case = self.get_slot_data(x, y)
        case.is_robot = True
        case.empty = False

    # Temp pour test exploration
    def test_exploration(self):
        uninformed = Uninformed()
        informed = Informed()
        robot_x = self.robot_position_x
        robot_y = self.robot_position_y
        dest_x = 4
        dest_y = 4

        matrix_test = self.get_matrix()
        path = uninformed.calculate_path(robot_x, robot_y, dest_x, dest_y, matrix_test)
        print("Chemin non-informé : " + str(path))
        path_informed = informed.calculate_path(robot_x, robot_y, dest_x, dest_y, matrix_test)
        print("Chemin informé : " + str(path_informed))
