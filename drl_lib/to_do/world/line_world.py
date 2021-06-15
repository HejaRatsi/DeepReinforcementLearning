import numpy as np


#DEFINITION DU LINE WORLD SOUS LA FORME D'UN MDP


MAX_CELLS = 7

# - identfier l'ensemble des états possibles
S = np.arange(MAX_CELLS)

# - identfier l'ensemble des actions possibles
A = np.array([0, 1])  # 0: Gauche, 1: Droite

# - identfier l'ensemble des rewards (gains) possibles
R = np.array([-1, 0, 1])


# - identifier le p(s r | s a) => LES REGLES DU JEU
p = np.zeros((len(S), len(A), len(S), len(R)))

for i in range(1, MAX_CELLS - 2):
    p[i, 1, i + 1, 1] = 1.0

for i in range(2, MAX_CELLS - 1):
    p[i, 0, i - 1, 1] = 1.0

p[MAX_CELLS - 2, 1, MAX_CELLS - 1, 2] = 1.0
p[1, 0, 0, 0] = 1.0