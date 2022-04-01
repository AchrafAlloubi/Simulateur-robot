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


class Rules:


    def __call__(self) -> None:
        return

    def trigger_identify_fire(self) -> None:
        """
        On se met en mode éteindre le feu
        """
        return

    def trigger_identify_rubble(self):
        """
        On a détecter de la poussière, on doit
        """
        return

    def trigger_rescues(self):
        """
        On a détecter de la poussière, on doit
        """
        return