"""
Regroupe les principaux concepts vue en classe:
DDI
Etat
Metrique
"""
from dbi.believe import Believe
from dbi.desire import Desire
from dbi.intention import Intention


class IntelligentAgent:
    believe = Believe()
    desire = Desire()
    intention = Intention()

    def __call__(self) -> None:
        return

    def execute_best_move(self):
        """
        Algorithme principale de l'agent
        """

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
