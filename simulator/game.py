"""
Simulateur
"""
from time import sleep

from expert_system.inference_engine import InferenceEngine
from simulator.display import Display
from simulator.level_generator import LevelGenerator
from tweak import Tweak


class Game:
    tweak = Tweak()
    display = Display()
    game_over = False
    level = 1
    map_size = Tweak.environment_start_length

    def start(self):

        self.display.print_main_title()
        while not self.game_over:
            # Menu
            self.display.print_level_title(self.level, self.map_size)
            self.display.print_legend()

            # Génération de la map
            level_generator = LevelGenerator(self.map_size)
            level_generator.environment.set_robot_position(Tweak.robot_start_x, Tweak.robot_start_y)
            level_generator.generate_map()

            self.display.print_map(level_generator.environment)

            # Robot est un System expert
            robot = InferenceEngine()

            while not robot.facts.survival_is_secured:
                # Filtrage
                robot.filter(level_generator.environment)
                # Choix de la règle
                action = robot.choose_rule()
                # Application de la règle
                robot.apply_rule(action, level_generator.environment)

                if Tweak().debug:
                    # Utile pour le débuggage
                    self.display.print_map(level_generator.environment)
                    sleep(Tweak().robot_loop_sleep)

                if robot.facts.survival_is_secured:
                    print("Trouvé le survivant")

                if not robot.facts.am_i_alive:
                    self.game_over = True
                    exit("FIN : Robot est mort dans les décombres")


            input("Appuyez sur Entrée pour passer au niveau suivant")

            self.level += 1
            self.map_size += 1
            robot.facts.survival_is_secured = False
