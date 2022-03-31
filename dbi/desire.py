"""
C'est l'algorithme de recherche
"""
from dbi.state import State
from exploration.informed import Informed
from exploration.uninformed import Uninformed

"""
Légende: Actions Robot
0-Gauche
1-Droite
2-Haut
3-Bas
4-Aspirer
5-Cueillir
"""

class Desire:
    def __call__(self) -> None:
        return

    def execute_exploration(self, state: State) -> []:

        # Est-ce que l'agent à accomplis son objectif ?
        if state.all_peace_is_clean:
            print("Travail terminé !")
            return []

        next_object = state.object_available[0]
        dest_x = next_object[0]
        dest_y = next_object[1]
        #print("robot_x:" + str(state.x))
        #print("robot_y:" + str(state.y))
        #print("destination_x:" + str(dest_x))
        #print("destination_y:" + str(dest_y))

        if not state.exploration_informed :
            uninformed = Uninformed()
            path = uninformed.calculate_path(state.x,  state.y, dest_x, dest_y, state.matrix)
            print("Chemin non-informé : " + str(path))
            return path
        else:
            informed = Informed()
            path = informed.calculate_path(state.x, state.y, dest_x, dest_y, state.matrix)
            print("Chemin informé : " + str(path))
            return path


