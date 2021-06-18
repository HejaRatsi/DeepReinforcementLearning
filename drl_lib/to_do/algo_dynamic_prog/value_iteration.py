import numpy as np
import random


def value_iteration(lenS, S, A, R, P):
    # for line world_dynamic_prog
    # lenS   => len(States_LineW)
    # S      => States_LineW

    # for grid world_dynamic_prog
    # lenS   => MAX_CELLS_GridW
    # S      => range(MAX_CELLS_GridW)

    V = np.zeros((lenS,))

    theta = 0.0001
    gamma = 0.9999
    while True:
        delta = 0
        for s in S:
            v = V[s]
            V[s] = 0
            max_cumul_A = 0
            for a in A:
                cumul_A = 0
                for s_p in S:
                    for r_idx, r in enumerate(R):
                        cumul_A += P[s, a, s_p, r_idx] * (r + gamma * V[s_p])

                if cumul_A > max_cumul_A:
                    max_cumul_A = cumul_A

            V[s] = max_cumul_A

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break

    # ----------------------------------------OUTPUT A DETERMINITSI POLICY----------------------------------------
    # ----------------------------------------OUTPUT A DETERMINITSI POLICY----------------------------------------

    pi = np.zeros((lenS, len(A)))

    for s in S:
        best_a = -1
        best_a_score = None

        for a in A:
            a_score = 0.0
            for s_p in S:
                for r_idx, r in enumerate(R):
                    a_score += P[s, a, s_p, r_idx] * (r + gamma * V[s_p])
            if best_a_score is None or best_a_score < a_score:
                best_a = a
                best_a_score = a_score
        pi[s, :] = 0.0
        pi[s, best_a] = 1.0

    return pi, V



