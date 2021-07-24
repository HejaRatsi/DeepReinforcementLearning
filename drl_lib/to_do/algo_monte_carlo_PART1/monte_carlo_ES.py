import numpy as np
from tqdm import tqdm
from dataclasses import dataclass

from drl_lib.to_do.world_monteCarlo_and_temporalDiff_PART1.contratSingleAgentEnv import SingleAgentEnv


@dataclass
class PolicyAndActionValueFunction:
    pi: dict[int, dict[int, float]]
    q: dict[int, dict[int, float]]


def monte_carlo_ES(
        env: SingleAgentEnv,
        epsilon: float,
        gamma: float,
        max_iter: int) -> PolicyAndActionValueFunction:
    pi = {}
    q = {}
    returns = {}

    for it in tqdm(range(max_iter)):
        env.reset()
        S = []
        A = []
        R = []
        # !!!!!! ALGO STEP !!!!!!
        # Choose S0,A0 randomly such that all pairs have probability > 0 (in algo)
        s0 = env.state_id()
        S.append(s0)
        available_actions = env.available_actions_ids()
        if s0 not in pi:
            pi[s0] = {}
            q[s0] = {}
            returns[s0] = {}
            for a in available_actions:
                pi[s0][a] = 1.0 / len(available_actions)
                q[s0][a] = 0.0
                returns[s0][a] = []
        available_actions = env.available_actions_ids()

        chosen_action = np.random.choice(available_actions)

        # print("Choosen action first "+str(chosen_action))
        A.append(chosen_action)
        old_score = env.score()
        env.act_with_action_id(chosen_action)
        r = env.score() - old_score
        R.append(r)

        # !!!!!! ALGO STEP !!!!!!
        # Generate an episode from S0,A0 folowing pi: S0, A0, R1,....,RT (in algo)
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
            # chosen_action = np.random.choice(available_actions)

            A.append(chosen_action)
            old_score = env.score()
            env.act_with_action_id(chosen_action)
            r = env.score() - old_score
            R.append(r)

        # !!!!!! ALGO STEP !!!!!!
        # G <- 0 (in algo)
        G = 0
        # Loop for each step of episode... (in algo)
        for t in reversed(range(len(S))):
            G = gamma * G + R[t]
            # Unless the pair St, At apperas... (in algo)
            s_t = S[t]
            a_t = A[t]
            found = False
            for p_s, p_a in zip(S[:t], A[:t]):
                if s_t == p_s and a_t == p_a:
                    found = True
                    break
            if found:
                continue

            # !!!!!! ALGO STEP !!!!!!
            # Append G t returns(St, At) (in algo)
            returns[s_t][a_t].append(G)
            q[s_t][a_t] = np.mean(returns[s_t][a_t])

            # !!!!!! ALGO STEP !!!!!!
            # pi[s_t] <- argmaxa Q(St,a) (in algo)

            optimal_a_t = list(q[s_t].keys())[np.argmax(list(q[s_t].values()))]

            # !!!!!! ALGO STEP !!!!!!
            # For all a ... (in algo)
            for a_key, q_s_a in q[s_t].items():
                if a_key == optimal_a_t:
                    pi[s_t][a_key] = 1.0
                else:
                    pi[s_t][a_key] = 0.0

    return PolicyAndActionValueFunction(pi, q)

