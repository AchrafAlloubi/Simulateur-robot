"""
Robot
"""
from expert_system.inference_engine import InferenceEngine
from robot.actuators import Actuators
from robot.sensors import Sensors
from simulator.case import Case
from simulator.environment import Environment
from simulator.action import Action


class Robot(InferenceEngine):
    name = 'Robot qui sauve des vies'

    def use_all_sensors_on_environment(self, global_environment: Environment) -> None:
        # Conserve la position du robot
        self.facts.current_x = global_environment.robot_position_x
        self.facts.current_y = global_environment.robot_position_y

        # Utilise les sensors sur l'environment
        sensors = Sensors(global_environment)

        # Conserve les cases adjacentes dans les facts
        self.facts.adjacent_cases = sensors.adjacent_cases

        # Concerve des faits qui lance des règles au besoins
        self.set_cry_cases(sensors.use_microphone())
        self.set_hot_cases(sensors.detect_heat())
        self.set_dust_cases(sensors.detect_dust())

    def exectute_best_action(self, global_environment: Environment) -> None:
        action = self.get_best_action()
        print('Action:', action.description, action.direction)
        actuators = Actuators(global_environment)

        if action.description == 'MOVE' and action.direction == 'UP':
            actuators.move_up()
        if action.description == 'MOVE' and action.direction == 'DOWN':
            actuators.move_down()
        if action.description == 'MOVE' and action.direction == 'LEFT':
            actuators.move_left()
        if action.description == 'MOVE' and action.direction == 'RIGHT':
            actuators.move_right()

        # Si on pile sur des décombres et qu'on a pas été capable de les identifiers, on est mort
        if action.destination_case.is_rubble and not actuators.identify_rubble():
            self.facts.am_i_alive = False

        if action.description == 'FIRE':
            actuators.use_extinguisher(action.destination_case)

        if action.description == 'SURVIVOR':
            self.facts.survival_is_secured = True

