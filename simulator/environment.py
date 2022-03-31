"""
Légende: Data Environnement
0-Case Vide
1-Case Poussière
2-Case Bijou
3-Case Poussière+Bijou
10-Case Joueur
"""

from exploration.informed import Informed
from exploration.uninformed import Uninformed


class Environment:
    length_x = 5
    length_y = 5
    matrix = []
    robot_position_y = None
    robot_position_x = None

    def __call__(self) -> None:
        return

    def __init__(self, length_x, length_y, robot_x, robot_y) -> None:
        self.length_x = length_x
        self.length_y = length_y
        self.create_matrix()
        self.set_robot_position(robot_x, robot_y)
        return

    def create_matrix(self):
        print(self.length_x)
        self.matrix = []
        for y in range(self.length_y):
            self.matrix.append([])
            for x in range(self.length_x):
                self.matrix[y].append(0)

    def get_matrix(self):
        # Copie de la matrice
        matrix_robot = []
        for y in range(len(self.matrix)):
            matrix_robot.append([])
            for x in range(len(self.matrix[y])):
                matrix_robot[y].append(self.matrix[y][x])

        # matrix_robot[3][2] = 1
        #matrix_robot[0][0] = 1
        #matrix_robot[1][1] = 1
        #matrix_robot[2][2] = 1
        #matrix_robot[3][3] = 1
        #matrix_robot[4][4] = 1
        # matrix_robot[4][4] = 1 #Fonctionne, retourne [1, 1, 1, 2, 2, 2]

        # Ajout du joueur
        if self.contained_matrix(self.robot_position_x, self.robot_position_y, matrix_robot):
            matrix_robot[self.robot_position_y][self.robot_position_x] += 10

        return matrix_robot

    def contained_matrix(self, pos_x, pos_y, matrix):
        if pos_y >= len(matrix) or pos_y < 0:
            return False
        if pos_x >= len(matrix[len(matrix)-1]) or pos_x < 0:
            return False
        return True

    def get_slot_data(self, x, y):
        return self.matrix[y][x]

    def add_slot_data(self, x, y, data_id):
        slot_id = self.matrix[y][x]
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

    def get_size_x(self):
        return self.length_x

    def get_size_y(self):
        return self.length_y

    def set_robot_position(self, x, y):
        self.robot_position_x = x
        self.robot_position_y = y

    #Temp pour test exploration
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
