import numpy as np


#DEFINITION DU GRID WORLD SOUS LA FORME D'UN MDP


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
for i in range((ONE_LINE_CELL * 3) - 1, ONE_LINE_CELL * (ONE_LINE_CELL - 1), 5):
        P_GridW[i,2,i-5,1] = 1.0

for j in range(0,ONE_LINE_CELL-1):
    for i in range(ONE_LINE_CELL+j,(ONE_LINE_CELL*ONE_LINE_CELL)+j,5):
        P_GridW[i,2,i-5,1] = 1.0

#bas
for i in range((ONE_LINE_CELL * 2) - 1, ONE_LINE_CELL * (ONE_LINE_CELL - 2), 5):
        P_GridW[i,3,i+5,1] = 1.0

for j in range(0,ONE_LINE_CELL-1):
    for i in range(0+j,ONE_LINE_CELL*(ONE_LINE_CELL-1)+j,5):
        P_GridW[i,3,i+5,1] = 1.0



#Je perd
P_GridW[ONE_LINE_CELL-2,1,ONE_LINE_CELL-1,0] = 1.0
P_GridW[(ONE_LINE_CELL*2)-1,2,ONE_LINE_CELL-1,0] = 1.0

#Je gagne
P_GridW[(ONE_LINE_CELL*4)-1,3,MAX_CELLS_GridW-1,2] = 1.0
P_GridW[MAX_CELLS_GridW-2,1,MAX_CELLS_GridW-1,2] = 1.0


