import numpy as np
from tqdm import tqdm
from dataclasses import dataclass

from drl_lib.to_do.world_monteCarlo_and_temporalDiff_PART1.contratSingleAgentEnv import SingleAgentEnv


@dataclass
class PolicyAndActionValueFunction:
    pi: dict[int, dict[int, float]]
    q: dict[int, dict[int, float]]
    #c: dict[int, dict[int, float]]
    #b: dict[int, dict[int, float]]


def off_policy_monte_carlo_control(
        env: SingleAgentEnv,
        epsilon: float,
        gamma: float,
        max_iter: int) -> PolicyAndActionValueFunction:

    #Initialization

    #Q(s,a)
    q = {}
    #C(s,a)
    c = {}
    #PI(s) (argmax...)
    pi = {}



    #Loop forever
    for it in tqdm(range(max_iter)):
        env.reset()
        S = []
        A = []
        R = []
        #b <- any soft policy
        b = {}
        # Generate an episode following b : S0, A0, R1,....,RT (in algo)
        while not env.is_game_over():
            s = env.state_id()
            S.append(s)
            available_actions = env.available_actions_ids()
            if s not in b:
                b[s] = {}
                #q[s] = {}
                #c[s] = {}
                for a in available_actions:
                    b[s][a] = 1.0 / len(available_actions)
                    #q[s][a] = 0.0
                    #c[s][a] = 0.0
            chosen_action = np.random.choice(
                list(b[s].keys()),
                1,
                False,
                p=list(b[s].values())
            )[0]
            #added by me-----------------------------------------------#
            if s not in pi:
                pi[s] = {}
                q[s] = {}
                c[s] = {}
                for a in available_actions:
                    pi[s][a] = 1.0 / len(available_actions)
                    q[s][a] = 0.0
                    c[s][a] = 0.0
            #added by me-----------------------------------------------#

            A.append(chosen_action)
            old_score = env.score()
            env.act_with_action_id(chosen_action)
            r = env.score() - old_score
            R.append(r)

        #Q <- 0
        G = 0
        #W <- 1
        W = 1

        # Loop for each step of episode... (in algo)
        for t in reversed(range(len(S))):
            G = gamma * G + R[t]
            s_t = S[t]
            a_t = A[t]
            #print("Voici la valeur "+str(c[s_t][a_t]))
            c[s_t][a_t] = c[s_t][a_t] + W
            temp = (W / c[s_t][a_t]) * (G - q[s_t][a_t])
            """
            print("Le W "+str(W))
            print("Attention au 0 le c[s_t][a_t] " + str(c[s_t][a_t]))
            print("Attention au 0 le b[s_t][a_t] " + str(b[s_t][a_t]))
            print("Le g "+str(G))
            print("Le temp "+str(temp))
            """
            q[s_t][a_t] = q[s_t][a_t] + temp
            #print("le q[s_t][a_t] " + str(q[s_t][a_t]))

            #pi(s_t) <- argmax....
            optimal_a_t = list(q[s_t].keys())[np.argmax(list(q[s_t].values()))]
            #pi[s_t] = {}

            for a_key, q_s_a in q[s_t].items():
                if a_key == optimal_a_t:
                    pi[s_t][a_key] = 1.0
                else:
                    pi[s_t][a_key] = 0.0

            #if At...
            if a_t != optimal_a_t:
                break


            #W <- W*1/...
            W = W * (1/b[s_t][a_t])

    return PolicyAndActionValueFunction(pi, q)#, c, b)

