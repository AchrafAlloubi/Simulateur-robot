"""
Générateur des tableaux
"""
import random
from time import sleep

from simulator.environment import Environment
from tweak import Tweak


class LevelGenerator:
    map_length = None
    environment = None

    def __call__(self) -> None:
        return

    def __init__(self, map_length):
        random.seed()
        self.environment = Environment(map_length, map_length)
        self.map_length = map_length
        return

    def generate_map(self) -> None:

        things_need_to_be_placed = True
        survivor_is_placed = False
        fire_is_placed = False
        rubble_is_placed = False
        while things_need_to_be_placed:
            position = self.generate_random_position()
            case = self.environment.get_slot_data(position['x'], position['y'])
            adjacent_cases = self.environment.get_adjacent_cases(position['x'], position['y'])
            print_position = '(' + str(position['x']) + ',' + str(position['y']) + ')'

            if not case.empty:
                # Recommence pour trouver une autre case libre
                continue

            if not survivor_is_placed:
                if Tweak().debug:
                    print('Gens', print_position)
                case.is_survivor = True
                case.empty = False
                survivor_is_placed = True

                for case in adjacent_cases:
                    case.is_cry = True
                continue

            if not fire_is_placed:
                if Tweak().debug:
                    print('Feu', print_position)
                case.is_fire = True
                case.empty = False
                fire_is_placed = True

                for case in adjacent_cases:
                    case.is_hot = True
                continue

            if not rubble_is_placed:
                if Tweak().debug:
                    print('Décombres', print_position)
                case.is_rubble = True
                case.empty = False
                rubble_is_placed = True

                for case in adjacent_cases:
                    case.is_dust = True
                continue

            things_need_to_be_placed = False

    def get_map(self) -> []:
        return self.environment.matrix

    def generate_random_position(self) -> {}:
        random_x = random.randrange(0, self.map_length)
        random_y = random.randrange(0, self.map_length)
        position = {"x": random_x, "y": random_y}
        return position


    def get_environment_name(self):
        # todo retourner un nom au hasard : bâtiments en ruine et des bâtiments en feu ou même des villes victimes de catastrophes naturelles
        return

    def add_item(self, data_id):
        # random.seed()
        # rand_x = random.randrange(0, self.environment_controller.environment.get_size_x())
        # rand_y = random.randrange(0, self.environment_controller.environment.get_size_y())
        # self.environment_controller.add(rand_x, rand_y, data_id)
        return
