"""
Exécution des actions
"""

from communication.environment_controller import EnvironmentController
from robot.actuator import Actuator


class Intention:
    actuator = Actuator()
    environment_controller = EnvironmentController()

    def __call__(self,) -> None:
        return

    def execute_action_plan(self, action_plan: []) -> []:

        if not action_plan:
            print("Aucun plan d'action à faire")
            return []
        next_action = action_plan[0]
        print("print next move" + str(next_action))
        updated_metric = []

        if next_action == 0:
            self.actuator.move_left()
            updated_metric.append('move')
        if next_action == 1:
            self.actuator.move_right()
            updated_metric.append('move')
        if next_action == 2:
            self.actuator.move_up()
            updated_metric.append('move')
        if next_action == 3:
            self.actuator.move_down()
            updated_metric.append('move')
        if next_action == 4:
            # Aspirer
            matrix = self.environment_controller.environment.matrix
            robot_x = self.environment_controller.environment.robot_position_x
            robot_y = self.environment_controller.environment.robot_position_y
            if matrix[robot_y][robot_x] == '1':
                updated_metric.append('aspired_dust')
            elif matrix[robot_y][robot_x] == '3':
                updated_metric.append('aspired_dust')
                updated_metric.append('aspired_jewel')
            else:
                print("ERREUR: Tentative d'aspirer autre chose qu'une poussière ou une poussière + bijou")

            self.actuator.aspire(robot_x, robot_y)
        if next_action == 5:
            # Collecter
            matrix = self.environment_controller.environment.matrix
            robot_x = self.environment_controller.environment.robot_position_x
            robot_y = self.environment_controller.environment.robot_position_y
            if matrix[robot_y][robot_x] == '2':
                updated_metric.append('collected_jewel')
            else:
                print("ERREUR: Tentative de collecter autre chose qu'une bijou")
            self.actuator.collect(robot_x, robot_y)
        return updated_metric
