import numpy as np
import random


def policy_iteration(lenS, S, A, R, P):
    # for line world
    # lenS   => len(States_LineW)
    # S      => States_LineW

    # for grid world
    # lenS   => MAX_CELLS_GridW
    # S      => range(MAX_CELLS_GridW)



    # La stratégie/policy
    pi = np.zeros((lenS, len(A)))
    for s in S:
        pi[s, random.randint(0, len(A) - 1)] = 1.0

    # La value function
    V = np.zeros((lenS,))

    while True:
        # 2 : Policy Evaluation

        theta = 0.000001
        gamma = 0.99999

        while True:
            delta = 0
            for s in S:
                v = V[s]
                V[s] = 0
                for a in A:
                    for s_p in S:
                        for r_idx, r in enumerate(R):
                            V[s] += pi[s, a] * P[s, a, s_p, r_idx] * (r + gamma * V[s_p])
                delta = max(delta, abs(v - V[s]))

            if delta < theta:
                break

        # 3 : Policy Improvement
        policy_stable = True
        for s in S:
            old_state_policy = np.copy(pi[s, :])

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
            if not np.array_equal(old_state_policy, pi[s]):
                policy_stable = False
        if policy_stable:
            break

    return pi, V
