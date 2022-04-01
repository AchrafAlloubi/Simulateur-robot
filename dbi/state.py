"""
Tous les indicateurs de performance que le robot possède
"""
from dbi.metric import Metric
from simulator.simulator import Environment


class State:
    x = None
    y = None
    object_available = []
    matrix = None
    action_plan = None
    all_peace_is_clean = False
    exploration_informed = False


    def __call__(self) -> None:
        return

    def set_current_position(self, x, y) -> None:
        """
        Met à jour la position actuel du robot
        """
        self.x = x
        self.y = y

    def update(self, environment: Environment, metric: Metric) -> None:
        """
        Met à jour tous les états de l'agent
        """

        # self.set_current_position(environment.robot_position_x, environment.robot_position_y)
        self.x = environment.robot_position_x
        self.y = environment.robot_position_y

        # S'il contient toujours quelque chose dans les pièces
        if self.object_available:
            self.all_peace_is_clean = False
        else:
            self.all_peace_is_clean = True

        self.matrix = environment.matrix

        if metric.total_iteration > 5:
            self.exploration_informed = True

