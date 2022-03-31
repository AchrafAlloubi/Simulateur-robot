"""
Légende: Actions Robot
0-Gauche
1-Droite
2-Haut
3-Bas
4-Aspirer
5-Cueillir
"""
from exploration.grid_node import GridNode


class Uninformed:
    path = []
    pos_cour_x = 0
    pos_cour_y = 0
    diff_x = 0
    diff_y = 0

    def __call__(self) -> None:
        return

    def __init__(self):
        return

    # Params : Pos Robot - Pos Destination
    def calculate_path(self, robot_x, robot_y, dest_x, dest_y, matrix) -> []:
        self.pos_cour_x = robot_x
        self.pos_cour_y = robot_y
        self.path = []

        # Calcul Différentiel
        self.diff_x = dest_x - robot_x
        self.diff_y = dest_y - robot_y

        # Mouv X + Action
        while self.diff_x != 0:
            if self.diff_x > 0:
                self.move(1, 0, matrix)
            elif self.diff_x < 0:
                self.move(-1, 0, matrix)

        # Mouv Y + Action
        while self.diff_y != 0:
            if self.diff_y > 0:
                self.move(0, 1, matrix)
            elif self.diff_y < 0:
                self.move(0, -1, matrix)

        # Retourne chemin d'actions complet
        return self.path

    def move(self, move_x, move_y, matrix):
        # Mouvement
        self.pos_cour_x += move_x
        self.pos_cour_y += move_y
        self.diff_x -= move_x
        self.diff_y -= move_y
        if move_x < 0:
            self.path.append(0)
        if move_x > 0:
            self.path.append(1)
        if move_y > 0:
            self.path.append(2)
        if move_y < 0:
            self.path.append(3)

        # Check Actions
        if self.contains_dust(self.pos_cour_x, self.pos_cour_y, matrix):
            self.path.append(4)
        elif self.contains_jewel(self.pos_cour_x, self.pos_cour_y, matrix):
            self.path.append(5)

    def contains_dust(self, pos_x, pos_y, matrix):
        data_id = matrix[pos_y][pos_x]
        if data_id == 1 or data_id == 3:
            return True
        return False

    def contains_jewel(self, pos_x, pos_y, matrix):
        if matrix[pos_y][pos_x] == 2:
            return True
        return False
