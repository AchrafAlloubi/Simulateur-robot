"""
Paramètre pour ajuster le simulateur
"""


class Tweak:
    # Sleep en seconde
    refresh_display_loop_sleep = 2
    robot_loop_sleep = 3
    generator_loop_sleep = 4

    # % de génération
    dust_generation_rate = 30
    jewel_generation_rate = 5

    # Affichage
    debug = True

    def __call__(self) -> None:
        return
