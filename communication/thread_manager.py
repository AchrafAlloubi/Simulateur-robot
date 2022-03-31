"""
Gère les threads
"""
import threading
import time

from simulator import environment
from robot.robot import Robot
from simulator.generator import Generator


def robot_loop(sleep) -> None:
    """
    Boucle sans fin du robot
    """
    robot = Robot()

    while robot.am_i_alive:
        time.sleep(sleep)
        robot.execute()


def environment_generator_loop(sleep) -> None:
    """
    Boucle sans fin de l'environment
    """
    generator = Generator()
    generator.boot()

    while generator.am_i_alive:
        time.sleep(sleep)
        generator.execute()


class ThreadManager:

    def __call__(self) -> None:
        return

    def start_robot(self, robot_loop_sleep):
        """
        Démarre le thread du robot
        """

        robot = threading.Thread(target=robot_loop, args=(robot_loop_sleep,))
        robot.start()

    def start_generator(self, generator_loop_sleep):
        """
        Démarre le générateur de poussière et de bijou
        """
        # Programme le thread sur la function loop
        generator = threading.Thread(target=environment_generator_loop, args=(generator_loop_sleep,))
        generator.start()
