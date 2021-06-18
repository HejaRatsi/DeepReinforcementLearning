import numpy as np


#DEFINITION DU LINE WORLD SOUS LA FORME D'UN MDP



class LineWorld_DynamicProg:

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


    def make_rules(self):
        for i in range(1, self.ncell - 2):
            self.P_LineW[i, 1, i + 1, 1] = 1.0

        for i in range(2, self.ncell - 1):
            self.P_LineW[i, 0, i - 1, 1] = 1.0

        # Je gagne
        self.P_LineW[self.ncell - 2, 1, self.ncell - 1, 2] = 1.0
        # Je perd
        self.P_LineW[1, 0, 0, 0] = 1.0





















    """
    MAX_CELLS_LineW = 7

    # - identfier l'ensemble des états possibles
    States_LineW = np.arange(MAX_CELLS_LineW)

    # - identfier l'ensemble des actions possibles
    Actions_LineW = np.array([0, 1])  # 0: Gauche, 1: Droite

    # - identfier l'ensemble des rewards (gains) possibles
    Rewards_LineW = np.array([-1, 0, 1])


    #LES REGLES DU JEU
    # - identifier le p(s r | s a)
    P_LineW = np.zeros((len(States_LineW), len(Actions_LineW), len(States_LineW), len(Rewards_LineW)))
 
    for i in range(1, MAX_CELLS_LineW - 2):
        P_LineW[i, 1, i + 1, 1] = 1.0

    for i in range(2, MAX_CELLS_LineW - 1):
        P_LineW[i, 0, i - 1, 1] = 1.0

    #Je gagne
    P_LineW[MAX_CELLS_LineW - 2, 1, MAX_CELLS_LineW - 1, 2] = 1.0
    #Je perd
    P_LineW[1, 0, 0, 0] = 1.0
    """
