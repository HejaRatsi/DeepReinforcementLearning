from dataclasses import dataclass

import numpy as np
from tqdm import tqdm

from drl_lib.to_do.world_monteCarlo_and_temporalDiff_PART1.contratSingleAgentEnv import SingleAgentEnv


@dataclass
class PolicyAndActionValueFunction:
    pi: dict[int, dict[int, float]]
    q: dict[int, dict[int, float]]


def q_learning(
        env: SingleAgentEnv,
        alpha: float,
        epsilon: float,
        gamma: float,
        max_iter: int) -> PolicyAndActionValueFunction:
    assert (epsilon > 0)
    pi = {}  # learned greedy policy
    b = {}  # behaviour epsilon-greedy policy
    q = {}  # action-value function of pi


    # q[s][a]
    # {5: {0: 0.0, 1: 0.0}, 6: {0: 0.0, 1: 0.0}}
    # State_S: {Action_A1: Moyenne_récCum_deS_enfaisantA1_puis_policy, Actions_A2: Moyenne_récCum_deS_enfaisantA2_puis_policy}}


    #LOOP FOR EACH EPISODE (in algo)
    for it in tqdm(range(max_iter)):

        #INITIALIZE S (in algo)

        # pi, b, et q gardent leur valeur à chaque tour de boucle
        # s se réinitialise à chaque tour de boucle
        env.reset()



        #LOOP FOR EACH STEP OF EPISODE ... UNTIL S IS TERMINAL (in algo)
        while not env.is_game_over():
            # s est la position actuelle de l'agent
            s = env.state_id()
            # available_actions sont toutes les actions possibles (sauf en game over)
            available_actions = env.available_actions_ids()
            if s not in pi:
                pi[s] = {}
                q[s] = {}
                b[s] = {}
                for a in available_actions:
                    pi[s][a] = 1.0 / len(available_actions)
                    q[s][a] = 0.0
                    b[s][a] = 1.0 / len(available_actions)
            available_actions_count = len(available_actions)
            #CHOOSE A FROM S USING POLICY DERIVED... (in algo)

            # Accéder à un élement de la list q[s].keys()
            # l'élément à l'indice np.argmax(list(q[s].values()))
            # DONC l'action qui a la plus grande valeur pour l'état s

            #Exemple : q = {5: {0: 0.1, 1: 0.98}, 4: {0: 0.123, 1: 0.0}}
            #s = 5
            #Donc on prend l'action 1 car elle a 0.98 de valeur
            optimal_a = list(q[s].keys())[np.argmax(list(q[s].values()))]


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

            # MMMMEEEE
            for a_key, q_s_a in q[s].items():
                if a_key == optimal_a:
                    b[s][a_key] = 1 - epsilon + epsilon / available_actions_count
                else:
                    b[s][a_key] = epsilon / available_actions_count

            #TAKE ACTION A (in algo)
            chosen_action = np.random.choice(
                list(b[s].keys()),
                1,
                False,
                p=list(b[s].values())
            )[0]

            #OBSERVE R, S_p (in algo)
            old_score = env.score()
            env.act_with_action_id(chosen_action)
            r = env.score() - old_score
            s_p = env.state_id()
            next_available_actions = env.available_actions_ids()

            #Comme on a fait une action, on peut potentiellement etre en game over deja
            if env.is_game_over():
                q[s][chosen_action] += alpha * (r + 0.0 - q[s][chosen_action])
            else:
                if s_p not in pi:
                    #mettre le state dans le pi,q et b (reo le jamais reinialiser)
                    pi[s_p] = {}
                    q[s_p] = {}
                    b[s_p] = {}
                    for a in next_available_actions:
                        pi[s_p][a] = 1.0 / len(next_available_actions)
                        q[s_p][a] = 0.0
                        b[s_p][a] = 1.0 / len(next_available_actions)
                #Q(S,A) <- Q(S,A) + ...
                q[s][chosen_action] += alpha * (r + gamma * np.max(list(q[s_p].values())) - q[s][chosen_action])

    #print("STOP")
    #pour chaque state
    for s in q.keys():
        # Accéder à un élement de la list q[s].keys()
        # l'élément à l'indice np.argmax(list(q[s].values()))
        # DONC l'action qui a la plus grande valeur
        optimal_a = list(q[s].keys())[np.argmax(list(q[s].values()))]
        for a_key, q_s_a in q[s].items():
            if a_key == optimal_a:
                pi[s][a_key] = 1.0
            else:
                pi[s][a_key] = 0.0

    return PolicyAndActionValueFunction(pi, q)
