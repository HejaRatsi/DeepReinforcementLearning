import numpy as np


#DEFINITION DU LINE WORLD SOUS LA FORME D'UN MDP


MAX_CELLS = 7

# - identfier l'ensemble des états possibles
States_LineW = np.arange(MAX_CELLS)

# - identfier l'ensemble des actions possibles
Actions_LineW = np.array([0, 1])  # 0: Gauche, 1: Droite

# - identfier l'ensemble des rewards (gains) possibles
Rewards_LineW = np.array([-1, 0, 1])


# - identifier le p(s r | s a) => LES REGLES DU JEU
P_LineW = np.zeros((len(States_LineW), len(Actions_LineW), len(States_LineW), len(Rewards_LineW)))

for i in range(1, MAX_CELLS - 2):
    P_LineW[i, 1, i + 1, 1] = 1.0

for i in range(2, MAX_CELLS - 1):
    P_LineW[i, 0, i - 1, 1] = 1.0

P_LineW[MAX_CELLS - 2, 1, MAX_CELLS - 1, 2] = 1.0
P_LineW[1, 0, 0, 0] = 1.0