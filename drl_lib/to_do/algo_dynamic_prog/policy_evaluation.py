import numpy as np
import random

from drl_lib.to_do.world_dynamic_prog.contratMDP import ContratMDP


def policy_evalution(env: ContratMDP,pi,V):

    theta = 0.0001
    gamma = 0.9999

    while True:
        delta = 0
        for s in env.states():
            v = V[s]
            V[s] = 0
            # boucle sur les actions
            for a in env.actions():
                # boucle sur les états suivants possible
                for s_p in env.states():
                    # boucle sur les rewards
                    for r_idx, r in enumerate(env.rewards()):
                        tempVar = env.transition_probability(s, a, s_p, r_idx)
                        #tempVar = env.transition_probability(s, a, s_p, r_idx)
                        V[s] += pi[s, a] * tempVar * (r + gamma * V[s_p])
                        #V[s] += pi[s, a] * env.P[s, a, s_p, r_idx] * (r + gamma * V[s_p])

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break
    return V

