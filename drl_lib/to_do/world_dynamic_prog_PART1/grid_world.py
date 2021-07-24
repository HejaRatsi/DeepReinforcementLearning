import numpy as np

from drl_lib.to_do.world_dynamic_prog_PART1.contratMDP import ContratMDP

#DEFINITION DU GRID WORLD SOUS LA FORME D'UN MDP

class GridWorld_DynamicProg(ContratMDP):

    def __init__(self, oneLine: int):
        assert (oneLine > 0)
        self.oneLine = oneLine
        self.allLine = oneLine*oneLine
        # - identfier l'ensemble des états possibles
        self.States_GridW = np.arange(self.allLine)
        # - identfier l'ensemble des actions possibles
        self.Actions_GridW = np.array([0, 1, 2, 3])  # 0: Gauche, 1: Droite, 2:Haut, 3:Bas
        # - identfier l'ensemble des rewards (gains) possibles
        self.Rewards_GridW = np.array([-1, 0, 1])
        # LES REGLES DU JEU
        # - identifier le p(s r | s a)
        self.P_GridW = np.zeros((self.allLine, len(self.Actions_GridW), self.allLine, len(self.Rewards_GridW)))
        self.make_rules()


    def make_rules(self):
        #DROITE
        for i in range(0,self.oneLine-2):
            self.P_GridW[i,1,i+1,1] = 1.0
        for i in range(self.oneLine*(self.oneLine-1),self.allLine-2):
            self.P_GridW[i,1,i+1,1] = 1.0
        for i in range(self.oneLine,self.oneLine*(self.oneLine-1)-1):
            self.P_GridW[i,1,i+1,1] = 1.0
        #GAUCHE
        for i in range(1,self.oneLine-1):
            self.P_GridW[i,0,i-1,1] = 1.0
        for i in range(self.oneLine*(self.oneLine-1)+1,self.allLine-1):
            self.P_GridW[i,0,i-1,1] = 1.0
        for i in range(self.oneLine+1,self.oneLine*(self.oneLine-1)):
            self.P_GridW[i, 0, i - 1, 1] = 1.0
        #HAUT
        for i in range((self.oneLine * 3) - 1, self.oneLine * (self.oneLine - 1), self.oneLine):
            self.P_GridW[i, 2, i - self.oneLine, 1] = 1.0
        for j in range(0, self.oneLine - 1):
            for i in range(self.oneLine + j, (self.oneLine * self.oneLine) + j, self.oneLine):
                self.P_GridW[i,2,i-self.oneLine,1] = 1.0
        #BAS
        for i in range((self.oneLine * 2) - 1, self.oneLine * (self.oneLine - 2), self.oneLine):
            self.P_GridW[i, 3, i + self.oneLine, 1] = 1.0

        for j in range(0, self.oneLine - 1):
            for i in range(0 + j, self.oneLine * (self.oneLine - 1) + j, self.oneLine):
                self.P_GridW[i, 3, i + self.oneLine, 1] = 1.0

        #JE GAGNE
        self.P_GridW[self.allLine-2,1,self.allLine-1,2] = 1
        self.P_GridW[self.oneLine*(self.oneLine-1)-1,3,self.allLine-1,2] = 1
        #JE PERD
        self.P_GridW[(self.oneLine*2)-1,2,self.oneLine-1,0] = 1
        self.P_GridW[self.oneLine-2,1,self.oneLine-1,0] = 1



    def actions(self) -> np.ndarray:
        return self.Actions_GridW

    def rewards(self) -> np.ndarray:
        return self.Rewards_GridW

    def transition_probability(self, s: int, a: int, s_p: int, r_idx: int) -> int:
        return self.P_GridW[s, a, s_p, r_idx];

    def states(self) -> np.ndarray:
        return self.States_GridW


        # ADD DEFINE

    def is_state_terminal(self, s: int) -> bool:
        pass

    def view_state(self, s: int):
        pass





