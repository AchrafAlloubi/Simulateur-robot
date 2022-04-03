"""
Moteur d’inférence
"""
from expert_system.facts import Facts
from expert_system.rules import Rules
from simulator import environment


class InferenceEngine:
    facts = Facts()
    rules = Rules()
    current_strategy = None

    def __call__(self) -> None:
        return

    def __init__(self) -> None:
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
    def get_strategy(self, Environment: environment) -> None:
        """
        Algorithme principale de l'agent
        """
        environment


    def execute_best_move(self):


        # Récupère l'environment

        environment = self.believe.observe_environment_with_my_sensors()
        self.believe.state.update(environment, self.believe.metric)

        # Génère un plan d'action
        plan_action = self.desire.execute_exploration(self.believe.state)

        #Conserve le plan d'action dans son état
        self.believe.state.action_plan = plan_action

        # Exécution du plan d'action
        updated_metric = self.intention.execute_action_plan(plan_action)

        # Met à jour les métriques de l'agent
        self.believe.metric.update(updated_metric)
