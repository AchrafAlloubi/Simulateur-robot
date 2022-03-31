"""
Utilisé pour le calcul d'exploration informé (A* Pathfinding)
"""


class GridNode:
    path_parent = None  # Définit le parent le plus optimisé pour le pathfinding
    g_cost = 0
    h_cost = 0
    pos_x = 0
    pos_y = 0
    data_id = 0

    def __call__(self) -> None:
        return

    def __init__(self, pos_x, pos_y, data_id):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.data_id = data_id

    def f_cost(self):
        value = self.g_cost + self.h_cost
        if self.data_id == 1 or self.data_id == 3:
            value -= 5
        elif self.data_id == 2:
            value -= 8
        return value
