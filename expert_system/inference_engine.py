"""
Moteur d’inférence
"""


class InferenceEngine:
    current_strategy = None

    def __call__(self) -> None:
        return

    def filter(self) -> None:
        """
        Filtrage : Le Moteur d’Inférence (MI) compare l’état de la mémoire de travail avec les conditions des
        règles pour trouver l’ensemble des règles activables pour un niveau de l’arbre de possibilité
        """
    def choose_rule(self) -> None:
        """
        Choix d’une règle : Cette étape consiste à déduire de nouveaux faits en sélectionnant la règle la plus
        pertinente selon la stratégie

        TODO Je pense que c'est ici qu'on doit faire le chainage arrière
        """

    def apply_rule(self):
        """
        Appliquer la règle : Exécuter la règle sélectionnée en modifiant la base de faits
        """
    def get_strategy(self) -> None:
        """
        todo
        """
        return
