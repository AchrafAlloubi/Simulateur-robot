"""
Moteur d’inférence
"""
from expert_system.facts import Facts
from expert_system.rules import Rules
from simulator import environment
from simulator.case import Case
from simulator.action import Action


class InferenceEngine:
    facts = Facts()
    rules = Rules()
    current_strategy = None

    def __call__(self) -> None:
        return

    def __init__(self) -> None:
        return

    def get_best_action(self) -> Action:
        """
        Algorithme principale de l'agent
        """
        # TODO Doit mieux implémenter le système expert, pour l'instant, il se dirige vers le son, ensuite la chaleur, ensuite
        action = self.choose_rule()

        action.set_current_position(self.facts.current_x, self.facts.current_y)

        return action

    def set_cry_cases(self, cases_with_cry: []) -> None:
        if cases_with_cry:
            self.facts.cry_cases = cases_with_cry

    def set_hot_cases(self, cases_with_hot: []) -> None:
        if cases_with_hot:
            self.facts.hot_cases = cases_with_hot

    def set_dust_cases(self, cases_with_dust: []) -> None:
        if cases_with_dust:
            self.facts.dust_cases = cases_with_dust

    def filter(self) -> Case:
        """
        Filtrage : Le Moteur d’Inférence (MI) compare l’état de la mémoire de travail avec les conditions des
        règles pour trouver l’ensemble des règles activables pour un niveau de l’arbre de possibilité
        """

    def choose_rule(self) -> Action:
        """
        Choix d’une règle : Cette étape consiste à déduire de nouveaux faits en sélectionnant la règle la plus
        pertinente selon la stratégie

        TODO Je pense que c'est ici qu'on doit faire le chainage arrière
        """
        # todo aller vers le son

        # Sauve la vie du survivant
        for cases in self.facts.adjacent_cases:
            if cases.is_survivor:
                return Action('SURVIVOR', cases)

        # Éteind le feu
        for cases in self.facts.adjacent_cases:
            if cases.is_fire:
                return Action('FIRE', cases)

        # Se dirige vers les cris des survivants
        if self.facts.cry_cases:
            case = self.rules.trigger_rescues(self.facts.cry_cases)
            return Action('MOVE', case)

        # Se dirige vers la chaleur
        if self.facts.hot_cases:
            case = self.rules.trigger_identify_fire(self.facts.hot_cases)
            return Action('MOVE', case)

        # Se dirige la poussière
        if self.facts.dust_cases:
            case = self.rules.trigger_identify_rubble(self.facts.dust_cases)
            return Action('MOVE', case)

        # TODO Doit trouvé un chemin au hazard, j'ai pris la première
        return Action('MOVE', self.facts.adjacent_cases[0])

    def apply_rule(self):
        """
        Appliquer la règle : Exécuter la règle sélectionnée en modifiant la base de faits
        """

