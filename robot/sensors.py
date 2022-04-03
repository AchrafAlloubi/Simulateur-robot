"""
Représence ce que le robot voit
"""

from simulator.environment import Environment


class Sensors:
    adjacent_cases = []

    def __init__(self, global_environment: Environment) -> None:
        """
        L'agent ne peut voir que les cellules adjacentes à la position actuelle
        """
        x = global_environment.robot_position_x
        y = global_environment.robot_position_y
        self.adjacent_cases = global_environment.get_adjacent_cases(x, y)

    def detect_heat(self) -> []:
        """
        Si une des cases autours a de la chaleur
        """
        detected = []
        for case in self.adjacent_cases:
            if case.is_hot:
                detected.append(case)
        return detected

    def detect_dust(self) -> []:
        """
        Si une des cases autours a de la poussière
        """
        detected = []
        for case in self.adjacent_cases:
            if case.is_dust:
                detected.append(case)
        return detected

    def use_microphone(self) -> []:
        """
        Si on entend crier
        """
        detected = []
        for case in self.adjacent_cases:
            if case.is_cry:
                detected.append(case)
        return detected

    def identify_rubble(self):
        # Todo Lors de la détection de décombres, vous devez esquiver pour ne pas rester coincé
        return