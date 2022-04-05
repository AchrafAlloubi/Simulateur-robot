"""
Connaissances assertionnelles (Les faits)

todo : Liste des faits:
Position du robot
Nombre de chaleur à proximité
Nombre de poussière à proximité
Est piégé
A sauvé le survivant
"""
# todo se_situer(singe, D)

from simulator.environment import Environment


class Facts:
    current_x = None
    current_y = None
    current_case = None
    adjacent_cases = []
    visited_cases = []
    map = []
    cry_cases = []
    hot_cases = []
    dust_cases = []
    survival_is_secured = False
    am_i_alive = True
