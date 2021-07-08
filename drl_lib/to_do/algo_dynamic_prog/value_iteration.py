import numpy as np
import random

from drl_lib.to_do.world_dynamic_prog.contratMDP import ContratMDP


def value_iteration(env: ContratMDP):

    # La value function
    V = np.zeros((len(env.states()),))

    theta = 0.0001
    gamma = 0.9999
    while True:
        delta = 0
        for s in env.states():
            v = V[s]
            V[s] = 0
            max_cumul_A = 0
            for a in env.actions():
                cumul_A = 0
                for s_p in env.states():
                    for r_idx, r in enumerate(env.rewards()):
                        tempVar = env.transition_probability(s, a, s_p, r_idx)
                        #tempVar = env.transition_probability(s, a, s_p, r_idx)
                        cumul_A += tempVar * (r + gamma * V[s_p])
                        #cumul_A += env.P[s, a, s_p, r_idx] * (r + gamma * V[s_p])

                if cumul_A > max_cumul_A:
                    max_cumul_A = cumul_A

            V[s] = max_cumul_A

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break

    # ----------------------------------------OUTPUT A DETERMINITSI POLICY----------------------------------------
    # ----------------------------------------OUTPUT A DETERMINITSI POLICY----------------------------------------

    pi = np.zeros((len(env.states()), len(env.actions())))

    for s in env.states():
        best_a = -1
        best_a_score = None

        for a in env.actions():
            a_score = 0.0
            for s_p in env.states():
                for r_idx, r in enumerate(env.rewards()):
                    tempVar2 = env.transition_probability(s, a, s_p, r_idx)
                    #tempVar2 = env.transition_probability(s, a, s_p, r_idx)
                    a_score += tempVar2 * (r + gamma * V[s_p])
                    #a_score += env.P[s, a, s_p, r_idx] * (r + gamma * V[s_p])
            if best_a_score is None or best_a_score < a_score:
                best_a = a
                best_a_score = a_score
        pi[s, :] = 0.0
        pi[s, best_a] = 1.0

    return pi, V



