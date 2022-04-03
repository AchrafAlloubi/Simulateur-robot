"""
Robot
"""
from expert_system.inference_engine import InferenceEngine
from robot.actuators import Actuators
from robot.sensors import Sensors
from simulator.case import Case
from simulator.environment import Environment


class Robot(InferenceEngine):
    am_i_alive = 1
    name = 'Robot qui sauve des vies'
    actuator = Actuators()

    def use_all_sensors_on_environment(self, global_environment: Environment) -> None:
        sensors = Sensors(global_environment)

        cases_with_cry = sensors.use_microphone()
        cases_with_hot = sensors.detect_heat()
        cases_with_dust = sensors.detect_dust()

        print("TODO Ajouter au faits")

    def best_case_to_use_actuator(self) -> Case:
        #
        plan = self.get_strategy()

        return
