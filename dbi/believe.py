from dbi.metric import Metric
from dbi.state import State
from robot.sensor import Sensor

from simulator.game import Environment


class Believe:
    metric = Metric()
    state = State()
    sensor = Sensor()

    def __call__(self) -> None:
        return

    def observe_environment_with_my_sensors(self) -> Environment:
        """
        Entièrement observable
        """

        # Récupère tous les poussières et les bijoux existant
        self.state.object_available = self.sensor.get_dust_and_jewel()

        # Conserve la matrice dans son état interne
        return self.sensor.get_environment()
