"""
Robot
"""
from dbi.intelligent_agent import IntelligentAgent


class Robot(IntelligentAgent):
    am_i_alive = 1
    name = 'Aspirobot T-0.1'

    def __call__(self) -> None:
        print("Name :", self.name)
        return

    def boot(self) -> None:
        """
        Démarre le robot
        """
        print("Boot Robot")
        print("Name :", self.name)

    def execute(self) -> None:
        self.execute_best_move()
