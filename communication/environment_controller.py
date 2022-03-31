"""
Controller pour utiliser l'environement
Rend l'écriture dans l'environment thread safe
"""

from simulator.environment import Environment
from threading import Lock


class EnvironmentController:
    environment = Environment(5, 5, 2, 2)
    lock = Lock()
    # TODO Doit implémenter : Agent et generateur doivent rafraichir l'écran
    need_screen_refresh = True

    def __call__(self) -> None:
        return

    def add(self, x, y, data_id) -> None:
        # Pour gérer le multithread
        self.lock.acquire()
        self.environment.add_slot_data(x, y, data_id)
        self.lock.release()
        # self.need_screen_refresh = True

    def set_robot_position(self, x, y) -> None:
        self.lock.acquire()
        self.environment.set_robot_position()
        self.lock.release()
        # self.need_screen_refresh = True

    def clear_piece(self, x, y) -> None:
        print ("clear"+x+","+y)
        self.lock.acquire()
        self.environment.matrix[y][x] = 0
        self.lock.release()
