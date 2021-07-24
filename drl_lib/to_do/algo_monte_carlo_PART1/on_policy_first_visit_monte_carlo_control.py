import numpy as np
from tqdm import tqdm
from dataclasses import dataclass

from drl_lib.to_do.world_monteCarlo_and_temporalDiff_PART1.contratSingleAgentEnv import SingleAgentEnv


@dataclass
class PolicyAndActionValueFunction:
    pi: dict[int, dict[int, float]]
    q: dict[int, dict[int, float]]


def on_policy_first_visit_monte_carlo_control(
        env: SingleAgentEnv,
        epsilon: float,
        gamma: float,
        max_iter: int) -> PolicyAndActionValueFunction:
    #Initialize (in algo)
    pi = {}
    q = {}
    returns = {}

    for it in tqdm(range(max_iter)):
        env.reset()
        S = []
        A = []
        R = []
        # Generate an episode following pi : S0, A0, R1,....,RT (in algo)
        #print("START EPISODE")
        while not env.is_game_over():
            s = env.state_id()
            S.append(s)
            available_actions = env.available_actions_ids()
            if s not in pi:
                pi[s] = {}
                q[s] = {}
                returns[s] = {}
                for a in available_actions:
                    pi[s][a] = 1.0 / len(available_actions)
                    q[s][a] = 0.0
                    returns[s][a] = []
            chosen_action = np.random.choice(
                list(pi[s].keys()),
                1,
                False,
                p=list(pi[s].values())
            )[0]

            A.append(chosen_action)
            old_score = env.score()
            env.act_with_action_id(chosen_action)
            r = env.score() - old_score
            R.append(r)

        #print("END OF EPISODE")
        #G <- 0 (in algo)
        G = 0

        #Loop for each step of episode... (in algo)
        for t in reversed(range(len(S))):
                G = gamma * G + R[t]
                #Unless the pair St, At apperas... (in algo)
                s_t = S[t]
                a_t = A[t]
                found = False
                for p_s, p_a in zip(S[:t], A[:t]):
                    if s_t == p_s and a_t == p_a:
                        found = True
                        break
                if found:
                    continue
                #Append G t returns(St, At) (in algo)
                returns[s_t][a_t].append(G)
                q[s_t][a_t] = np.mean(returns[s_t][a_t])
                """
                            #MMMMEEEE
                            print("GO")
                            print(q) => {5: {0: 0.0, 1: 0.0}, 4: {0: 0.0, 1: 0.0}}
                            print(q[s]) => {0: 0.0, 1: 0.0}
                            print(q[s].items()) => dict_items([(0, 0.0), (1, 0.0)])
                            print(q[s].keys()) => dict_keys([0, 1])
                            print(q[s].values()) => dict_values([0.0, 0.0])
                            print("STOP")
                """
                #A* <- argmaxa Q(St,a) (in algo)
                optimal_a_t = list(q[s_t].keys())[np.argmax(list(q[s_t].values()))]
                available_actions_t_count = len(q[s_t])
                #For all a ... (in algo)
                for a_key, q_s_a in q[s_t].items():
                    if a_key == optimal_a_t:
                        pi[s_t][a_key] = 1 - epsilon + epsilon / available_actions_t_count
                    else:
                        pi[s_t][a_key] = epsilon / available_actions_t_count

    return PolicyAndActionValueFunction(pi, q)
