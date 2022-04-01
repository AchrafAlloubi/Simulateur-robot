"""
Paramètre pour ajuster le simulateur
"""


class Tweak:
    # Contrainte du TP
    environment_start_length = 3
    robot_start_x = 0
    robot_start_y = 0

    # Probabilité
    # Pourcentage de chance d'être piégé dans les décombres
    trapped_rate = 30
    # dust_generation_rate = 30
    # jewel_generation_rate = 5

    # Sleep en seconde
    refresh_display_loop_sleep = 2
    robot_loop_sleep = 3
    generator_loop_sleep = 4



    # Affichage
    debug = True




    def __call__(self) -> None:
        return
