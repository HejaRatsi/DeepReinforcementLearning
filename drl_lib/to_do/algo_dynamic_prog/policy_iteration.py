import numpy as np
import random

from drl_lib.to_do.world_dynamic_prog.contratMDP import ContratMDP


def policy_iteration(env: ContratMDP):

    # La stratégie/policy
    pi = np.zeros((len(env.states()), len(env.actions())))
    for s in env.states():
        pi[s, random.randint(0, len(env.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(env.states()),))

    while True:
        # 2 : Policy Evaluation

        theta = 0.000001
        gamma = 0.99999

        while True:
            delta = 0
            for s in env.states():
                v = V[s]
                V[s] = 0
                for a in env.actions():
                    for s_p in env.states():
                        for r_idx, r in enumerate(env.rewards()):
                            tempVar = env.transition_probability(s, a, s_p, r_idx)
                            #tempVar = env.transition_probability(s, a, s_p, r_idx)
                            V[s] += pi[s, a] * tempVar * (r + gamma * V[s_p])
                            #V[s] += pi[s, a] * env.P[s, a, s_p, r_idx] * (r + gamma * V[s_p])
                delta = max(delta, abs(v - V[s]))

            if delta < theta:
                break

        # 3 : Policy Improvement
        policy_stable = True
        for s in env.states():
            old_state_policy = np.copy(pi[s, :])

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
            if not np.array_equal(old_state_policy, pi[s]):
                policy_stable = False
        if policy_stable:
            break

    return pi, V
