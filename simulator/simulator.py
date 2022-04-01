"""
Simulateur
"""
from random import random

from robot.robot import Robot
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

    def start(self):

        display = Display()
        display.print_main_title()
        level_generator = LevelGenerator()
        matrix = level_generator.get_map(self.level)
        display.print_level_title(self.level, self.current_environment_length)
        display.print_legend()
        #display.print_map(matrix)
        #robot = Robot()
        print('TODO RENDU ICI')


