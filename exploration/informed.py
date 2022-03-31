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


class Informed:
    def __call__(self) -> None:
        return

    def __init__(self):
        return

    #Params : Pos Robot - Pos Destination
    def calculate_path(self, robot_x, robot_y, dest_x, dest_y, matrix) -> []:
        path_success = False
        grid = self.generate_grid(matrix)
        open_set = []
        closed_set = []

        #Obtention node début et fin
        start_node = grid[robot_y][robot_x]
        target_node = grid[dest_y][dest_x]
        self.generate_h_cost(grid, target_node)
        open_set.append(start_node)

        while len(open_set) > 0:
            cur_node = self.get_lowest_node(open_set)
            closed_set.append(cur_node)
            # print(" x:" + str(cur_node.pos_x) + " y:" + str(cur_node.pos_y))
            #Fin si node choisi est le noyau de fin
            if cur_node == target_node:
                path_success = True
                break

            #Analyse chaque voisin de la case courante
            for neighbour in self.get_neighbours(cur_node, grid):
                if self.is_closed(neighbour, closed_set):
                    continue
                #MAJ set de voisins si ouvert
                open_set = self.update_open_set(cur_node, neighbour, open_set)

        path = []
        if path_success:
            path = self.retrace_path(start_node, target_node)

        #Retourne le chemin d'actions à prendre
        return self.generate_action_plan(path)

    def contains_dust(self, pos_x, pos_y, matrix):
        data_id = matrix[pos_x, pos_y]
        if data_id == 4:
            return True
        return False

    def get_lowest_node(self, open_set):
        lowest_node = open_set[0]
        lowest_cost = lowest_node.f_cost()
        new_cost = 0
        for i in range(1, len(open_set)):
            new_cost = open_set[i].f_cost()
            if new_cost < lowest_cost:
                lowest_cost = new_cost
                lowest_node = open_set[i]
        #Retrait open node choisi
        open_set.remove(lowest_node)
        return lowest_node

    def get_neighbours(self, cur_node, grid):
        neighbours = []
        pos_x = cur_node.pos_x
        pos_y = cur_node.pos_y
        #Get all 4 directions
        if pos_x > 0:
            neighbours.append(grid[pos_y][pos_x-1])
        if pos_x < (len(grid[pos_y]) - 1):
            neighbours.append(grid[pos_y][pos_x+1])
        if pos_y > 0:
            neighbours.append(grid[pos_y-1][pos_x])
        if pos_y < (len(grid) - 1):
            neighbours.append(grid[pos_y+1][pos_x])
        #Return Neighbours
        return neighbours

    def generate_grid(self, matrix):
        grid = []
        for y in range(len(matrix)):
            grid.append([])
            for x in range(len(matrix[y])):
                grid[y].append(GridNode(x, y, matrix[y][x]))
        return grid

    def generate_h_cost(self, grid, target_node):
        for grid_y in grid:
            for node in grid_y:
                if node is not target_node:
                    node.h_cost = self.get_distance(node, target_node)

    def is_closed(self, node, closed_set):
        for closed in closed_set:
            if node == closed:
                return True
        return False

    def update_open_set(self, cur_node, neighbour, open_set):
        new_g_cost = 10 + cur_node.g_cost
        #Update if cost is undefined or more optimised
        if new_g_cost < neighbour.g_cost or neighbour.g_cost == 0:
            if neighbour.g_cost == 0: #Ajoute au Open set si pas présent
                open_set.append(neighbour)
            neighbour.g_cost = new_g_cost
            neighbour.path_parent = cur_node
        return open_set

    def get_distance(self, node_a, node_b):
        dist_x = abs(node_a.pos_x - node_b.pos_x)
        dist_y = abs(node_a.pos_y - node_b.pos_y)
        return (dist_x + dist_y) * 10

    def retrace_path(self, start_node, target_node):
        path = []
        cur_node = target_node
        #Calcul du chemin à prendre
        while cur_node != start_node:
            path.append(cur_node)
            cur_node = cur_node.path_parent #Get next node in path

        path.append(start_node)

        #Reverse path
        reversed_path = []
        for i in range(len(path)-1, -1, -1):
            reversed_path.append(path[i])
        return reversed_path

    def generate_action_plan(self, path):
        action_plan = []
        if (len(path) == 0):
            return action_plan

        dir_x = 0
        dir_y = 0

        prev_node = path[0]
        # Get direction + actions
        for i in range(len(path)):
            #Check Directions
            dir_x = path[i].pos_x - prev_node.pos_x
            dir_y = path[i].pos_y - prev_node.pos_y
            if dir_x < 0:  # Gauche
                action_plan.append(0)
            elif dir_x > 0:   #Droits
                action_plan.append(1)
            elif dir_y > 0:   #Haut
                action_plan.append(2)
            elif dir_y < 0:   #Bas
                action_plan.append(3)

            # Regarde si le robot doit aspirer/cueillir
            if path[i].data_id == 1 or path[i].data_id == 3:
                action_plan.append(4) #Aspirer Poussière
            elif path[i].data_id == 2:
                action_plan.append(5) #Cueillir Bijou

            prev_node = path[i]

        return action_plan
