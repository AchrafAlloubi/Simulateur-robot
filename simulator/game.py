"""
Simulateur
"""
from random import random
from time import sleep

from robot.robot import Robot
from simulator.display import Display
from simulator.level_generator import LevelGenerator
from tweak import Tweak


class Game:
    tweak = Tweak()
    display = Display()
    game_over = False
    level = 1
    map_size = Tweak.environment_start_length

    def __call__(self) -> None:
        return

    def start(self):
        display = Display()
        display.print_main_title()
        while not self.game_over:
            display.print_level_title(self.level, self.map_size)
            display.print_legend()
            level_generator = LevelGenerator(self.map_size)
            level_generator.environment.set_robot_position(Tweak.robot_start_x, Tweak.robot_start_y)
            level_generator.generate_map()

            display.print_map(level_generator.environment)

            robot = Robot()

            while not robot.facts.survival_is_secured:
                sleep(Tweak.robot_loop_sleep)
                robot.use_all_sensors_on_environment(level_generator.environment)
                robot.exectute_best_action(level_generator.environment)

                display.print_map(level_generator.environment)

                if robot.facts.survival_is_secured:
                    print("Trouvé le survivant")

                if not robot.facts.am_i_alive:
                    self.game_over = True
                    exit("FIN : Robot est mort dans les décombres")

            input("Appuyez sur Entrée pour passer au niveau suivant")

            self.level += 1
            self.map_size += 1
            robot.facts.survival_is_secured = False


