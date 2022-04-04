"""
Connaissances opérationnelles (Les règles)

Exemple de règle:
S'il y a deux chaleurs autour, alors la case en diagonal est nécessairement du feu (même chose pour les poussières / débris
Si feu à côté, doit l'éteindre
Si je suis piégé, je suis mort
Si je sauve la personne, j'atteind mon objectif et je termine le tableau
Si j'enlève le feu, les 4 chaleurs autours ne seront plus là
Si mon micro détecte du bruit, il y a un survivant proche
Si je détecte de la chaleur et des poussières, je préfère aller éteindre le feu
"""
# todo Est-ce qu'on préfère éteindre un feu ou fouiller des débris ?
import random

from simulator.case import Case
from simulator.action import Action


class Rules:

    def __call__(self) -> None:
        return

    def trigger_rescues(self, cases: []) -> Case:
        """
        On veut suivre le son pour secourir le survivant
        On utilise la probabilité pour choisir une direction au hazard
        """
        random.shuffle(cases)
        return cases.pop()

    def trigger_identify_fire(self, cases: []) -> Case:
        """
        On se met en mode éteindre le feu
        """
        random.shuffle(cases)
        return cases.pop()

    def trigger_identify_rubble(self, cases: []) -> Case:
        """
        On a détecter de la poussière, on doit
        """
        random.shuffle(cases)
        return cases.pop()
