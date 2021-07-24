import numpy as np


#DEFINITION DU LINE WORLD SOUS LA FORME D'UN MDP
from drl_lib.to_do.world_dynamic_prog_PART1.contratMDP import ContratMDP


class LineWorld_DynamicProg(ContratMDP):

    def __init__(self, number_total_cell: int):
        assert(number_total_cell > 0)
        self.ncell = number_total_cell
        # - identfier l'ensemble des états possibles
        self.States_LineW = np.arange(number_total_cell)
        # - identfier l'ensemble des actions possibles
        self.Actions_LineW = np.array([0, 1])  # 0: Gauche, 1: Droite
        # - identfier l'ensemble des rewards (gains) possibles
        self.Rewards_LineW = np.array([-1, 0, 1])
        # LES REGLES DU JEU
        # - identifier le p(s r | s a)
        self.P_LineW = np.zeros((len(self.States_LineW), len(self.Actions_LineW), len(self.States_LineW), len(self.Rewards_LineW)))
        self.make_rules()


        #self.lenS = len(self.States_LineW)


    def make_rules(self):
        for i in range(1, self.ncell - 2):
            self.P_LineW[i, 1, i + 1, 1] = 1.0


        for i in range(2, self.ncell - 1):
            self.P_LineW[i, 0, i - 1, 1] = 1.0

        # Je gagne
        self.P_LineW[self.ncell - 2, 1, self.ncell - 1, 2] = 1.0
        # Je perd
        self.P_LineW[1, 0, 0, 0] = 1.0



    def actions(self) -> np.ndarray:
        return self.Actions_LineW

    def rewards(self) -> np.ndarray:
        return self.Rewards_LineW

    def transition_probability(self,s: int, a: int, s_p: int, r_idx: int) -> int:
        return self.P_LineW[s, a, s_p, r_idx];

    def states(self) -> np.ndarray:
        return self.States_LineW


    # ADD DEFINE
    def is_state_terminal(self, s: int) -> bool:
        pass

    def view_state(self, s: int):
        pass















