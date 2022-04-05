"""
Moteur d’inférence
"""
import random

from expert_system.facts import Facts
from robot.actuators import Actuators
from robot.sensors import Sensors
from expert_system.action import Action
from simulator.environment import Environment


class InferenceEngine:
    facts = Facts()
    current_strategy = None

    def filter(self, global_environment: Environment) -> None:
        """
        Filtrage : Le Moteur d’Inférence (MI) compare l’état de la mémoire de travail avec les conditions des
        règles pour trouver l’ensemble des règles activables pour un niveau de l’arbre de possibilité
        """
        # Conserve la position du robot
        self.facts.current_x = global_environment.robot_position_x
        self.facts.current_y = global_environment.robot_position_y
        self.facts.current_case = global_environment.get_case(self.facts.current_x, self.facts.current_y)
        self.facts.visited_cases.append(self.facts.current_case)

        # Utilise les sensors sur l'environment
        sensors = Sensors(global_environment)

        # Conserve les cases adjacentes dans les facts
        self.facts.adjacent_cases = sensors.adjacent_cases

        # Concerve des faits sur les cases adjacentes
        self.facts.cry_cases = sensors.use_microphone()
        self.facts.hot_cases = sensors.detect_heat()
        self.facts.dust_cases = sensors.detect_dust()

    def choose_rule(self) -> Action:
        """
        Choix d’une règle : Cette étape consiste à déduire de nouveaux faits en sélectionnant la règle la plus
        pertinente selon la stratégie
        """

        # Sauve le survivant
        if self.facts.current_case.is_survivor:
            return Action('SAVE', self.facts.current_case)

        # Va vers le survivant
        for case in self.facts.adjacent_cases:
            if case.is_survivor:
                return Action('MOVE', case)

        # Éteind le feu
        for case in self.facts.adjacent_cases:
            if case.is_fire:
                return Action('FIRE', case)

        # Se dirige vers les cris des survivants
        if self.facts.cry_cases:
            random.shuffle(self.facts.cry_cases)
            case = self.facts.cry_cases.pop()
            return Action('MOVE', case)

        # Se dirige vers la chaleur
        if self.facts.hot_cases:
            random.shuffle(self.facts.hot_cases)
            case = self.facts.hot_cases.pop()
            return Action('MOVE', case)

        # Se dirige la poussière
        if self.facts.dust_cases:
            random.shuffle(self.facts.dust_cases)
            case = self.facts.dust_cases.pop()
            return Action('MOVE', case)

        # On visite une case jamais visité au hasard
        random.shuffle(self.facts.adjacent_cases)
        for adjacent_case in self.facts.adjacent_cases:
            visited = False
            for visited_case in self.facts.visited_cases:
                if adjacent_case is visited_case:
                    visited = True
            if not visited:
                return Action('MOVE', adjacent_case)

        # On a déjà tout visité les cases aux alentours, on va n'importe où...
        return Action('MOVE', self.facts.adjacent_cases[0])

    def apply_rule(self, action: Action, global_environment: Environment):
        """
        Appliquer la règle : Exécuter la règle sélectionnée en modifiant la base de faits
        """
        action.set_current_position(self.facts.current_x, self.facts.current_y)

        print(action.description, action.direction)
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

        if action.description == 'SAVE':
            self.facts.survival_is_secured = True
