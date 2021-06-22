import numpy as np


#DEFINITION DU GRID WORLD SOUS LA FORME D'UN MDP

class GridWorld_DynamicProg:

    def __init__(self, oneLine: int):
        assert (oneLine > 0)
        self.cell_one_line = oneLine
        self.cell_total = self.cell_one_line * self.cell_one_line
        # - identfier l'ensemble des états possibles
        self.States_GridW = self.define_states()
        # - identfier l'ensemble des actions possibles
        self.Actions_GridW = np.array([0, 1, 2, 3])  # 0: Gauche, 1: Droite, 2:Haut, 3:Bas
        # - identfier l'ensemble des rewards (gains) possibles
        self.Rewards_GridW = np.array([-1, 0, 1])
        # LES REGLES DU JEU
        # - identifier le p(s r | s a)
        self.P_GridW = np.zeros((self.cell_total, len(self.Actions_GridW), self.cell_total, len(self.Rewards_GridW)))
        self.make_rules()


        self.lenS = self.cell_total
        self.S = range(self.cell_total)
        self.A = self.Actions_GridW
        self.R = self.Rewards_GridW
        self.P = self.P_GridW
        self.zozo = 0


    def define_states(self):
        temp = np.arange(self.cell_one_line * self.cell_one_line)
        S = np.reshape(temp, (self.cell_one_line, self.cell_one_line))
        return S

    def make_rules(self):
        # droite
        for i in range(0, self.cell_one_line - 2):
            self.P_GridW[i, 1, i + 1, 1] = 1.0
        for j in range(1, self.cell_one_line - 1):
            for i in range(self.cell_one_line * j, (self.cell_one_line * (j + 1)) - 1):
                self.P_GridW[i, 1, i + 1, 1] = 1.0
        for i in range(self.cell_one_line * (self.cell_one_line - 1), self.cell_total - 2):
            self.P_GridW[i, 1, i + 1, 1] = 1.0
        # gauche
        for i in range(1, self.cell_one_line - 1):
            self.P_GridW[i, 0, i - 1, 1] = 1.0
        for j in range(1, self.cell_one_line - 1):
            for i in range((self.cell_one_line * j) + 1, (self.cell_one_line * (j + 1))):
                self.P_GridW[i, 1, i + 1, 1] = 1.0
        for i in range(self.cell_one_line * (self.cell_one_line - 1) + 1, self.cell_total - 1):
            self.P_GridW[i, 0, i - 1, 1] = 1.0
        # haut
        for i in range((self.cell_one_line * 3) - 1, self.cell_one_line * (self.cell_one_line - 1), self.cell_one_line):
            self.P_GridW[i, 2, i - self.cell_one_line, 1] = 1.0

        for j in range(0, self.cell_one_line - 1):
            for i in range(self.cell_one_line + j, (self.cell_one_line * self.cell_one_line) + j, self.cell_one_line):
                self.P_GridW[i, 2, i - self.cell_one_line, 1] = 1.0

        # bas
        for i in range((self.cell_one_line * 2) - 1, self.cell_one_line * (self.cell_one_line - 2), self.cell_one_line):
            self.P_GridW[i, 3, i + self.cell_one_line, 1] = 1.0

        for j in range(0, self.cell_one_line - 1):
            for i in range(0 + j, self.cell_one_line * (self.cell_one_line - 1) + j, self.cell_one_line):
                self.P_GridW[i, 3, i + self.cell_one_line, 1] = 1.0

        # Je perd
        self.P_GridW[self.cell_one_line - 2, 1, self.cell_one_line - 1, 0] = 1.0
        self.P_GridW[(self.cell_one_line * 2) - 1, 2, self.cell_one_line - 1, 0] = 1.0

        # Je gagne
        self.P_GridW[(self.cell_one_line * (self.cell_one_line - 1)) - 1, 3, self.cell_total - 1, 2] = 1.0
        self.P_GridW[self.cell_total - 2, 1, self.cell_total - 1, 2] = 1.0



    def transition_probability(self,s, a, s_p, r_idx):
        return self.P_GridW[s, a, s_p, r_idx];




















"""
#ICIIIII
ONE_LINE_CELL = 5
MAX_CELLS_GridW = ONE_LINE_CELL * ONE_LINE_CELL


# - identfier l'ensemble des états possibles
temp = np.arange(ONE_LINE_CELL * ONE_LINE_CELL)
States_GridW = np.reshape(temp, (ONE_LINE_CELL, ONE_LINE_CELL))


# - identfier l'ensemble des actions possibles
Actions_GridW = np.array([0, 1, 2, 3])  # 0: Gauche, 1: Droite, 2:Haut, 3:Bas


# - identfier l'ensemble des rewards (gains) possibles
Rewards_GridW = np.array([-1, 0, 1])





#LES REGLES DU JEU
# - identifier le p(s r | s a)
P_GridW = np.zeros((MAX_CELLS_GridW, len(Actions_GridW), MAX_CELLS_GridW, len(Rewards_GridW)))

#droite
for i in range(0,ONE_LINE_CELL-2):
    P_GridW[i,1,i+1,1] = 1.0
for j in range(1,ONE_LINE_CELL-1):
    for i in range(ONE_LINE_CELL*j,(ONE_LINE_CELL*(j+1))-1):
        P_GridW[i,1,i+1,1] = 1.0
for i in range(ONE_LINE_CELL*(ONE_LINE_CELL-1),MAX_CELLS_GridW-2):
    P_GridW[i,1,i+1,1] = 1.0
#gauche
for i in range(1,ONE_LINE_CELL-1):
    P_GridW[i,0,i-1,1] = 1.0
for j in range(1,ONE_LINE_CELL-1):
    for i in range((ONE_LINE_CELL*j)+1,(ONE_LINE_CELL*(j+1))):
        P_GridW[i,1,i+1,1] = 1.0
for i in range(ONE_LINE_CELL*(ONE_LINE_CELL-1)+1,MAX_CELLS_GridW-1):
    P_GridW[i,0,i-1,1] = 1.0
#haut
for i in range((ONE_LINE_CELL * 3) - 1, ONE_LINE_CELL * (ONE_LINE_CELL - 1), ONE_LINE_CELL):
        P_GridW[i,2,i-ONE_LINE_CELL,1] = 1.0

for j in range(0,ONE_LINE_CELL-1):
    for i in range(ONE_LINE_CELL+j,(ONE_LINE_CELL*ONE_LINE_CELL)+j,ONE_LINE_CELL):
        P_GridW[i,2,i-ONE_LINE_CELL,1] = 1.0

#bas
for i in range((ONE_LINE_CELL * 2) - 1, ONE_LINE_CELL * (ONE_LINE_CELL - 2), ONE_LINE_CELL):
        P_GridW[i,3,i+ONE_LINE_CELL,1] = 1.0

for j in range(0,ONE_LINE_CELL-1):
    for i in range(0+j,ONE_LINE_CELL*(ONE_LINE_CELL-1)+j,ONE_LINE_CELL):
        P_GridW[i,3,i+ONE_LINE_CELL,1] = 1.0



#Je perd
P_GridW[ONE_LINE_CELL-2,1,ONE_LINE_CELL-1,0] = 1.0
P_GridW[(ONE_LINE_CELL*2)-1,2,ONE_LINE_CELL-1,0] = 1.0

#Je gagne
P_GridW[(ONE_LINE_CELL*(ONE_LINE_CELL-1))-1,3,MAX_CELLS_GridW-1,2] = 1.0
P_GridW[MAX_CELLS_GridW-2,1,MAX_CELLS_GridW-1,2] = 1.0

"""