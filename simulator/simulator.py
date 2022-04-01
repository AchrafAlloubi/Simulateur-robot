"""
Simulateur
"""
from random import random

from simulator.display import Display
from simulator.level_generator import LevelGenerator
from tweak import Tweak


class Simulator:
    tweak = Tweak()
    display = Display()
    game_over = False
    level = 1
    current_environment_length = Tweak.environment_start_length
    

    def __call__(self) -> None:
        return
    def __init__(self):
        random.seed()
        return

    def start(self):
        tweak = Tweak()
        display = Display()
        display.print_title()
        level_generator = LevelGenerator()
        map = level_generator.get_map(self.level)
        print('TODO RENDU ICI')


