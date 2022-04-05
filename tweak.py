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
    robot_loop_sleep = 2

    # Affichage
    debug = False