import numpy as np
import random



def policy_evalution(env):#lenS, S, A, R, P):
    #for line world_dynamic_prog
    #lenS   => len(States_LineW)
    #S      => States_LineW

    #for grid world_dynamic_prog
    # lenS   => MAX_CELLS_GridW
    # S      => range(MAX_CELLS_GridW)


    # La stratégie/policy
    pi = np.zeros((env.lenS, len(env.A)))
    for s in env.S:
        pi[s, random.randint(0, len(env.A) - 1)] = 1.0

    # La value function
    V = np.zeros((env.lenS,))

    theta = 0.0001
    gamma = 0.9999

    while True:
        delta = 0
        for s in env.S:
            v = V[s]
            V[s] = 0
            # boucle sur les actions
            for a in env.A:
                # boucle sur les états suivants possible
                for s_p in env.S:
                    # boucle sur les rewards
                    for r_idx, r in enumerate(env.R):
                        V[s] += pi[s, a] * env.P[s, a, s_p, r_idx] * (r + gamma * V[s_p])

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break
    return V

