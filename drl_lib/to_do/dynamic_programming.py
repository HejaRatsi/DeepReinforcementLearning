from ..do_not_touch.mdp_env_wrapper import Env1
from ..do_not_touch.result_structures import ValueFunction, PolicyAndValueFunction
from ..to_do.world_dynamic_prog.line_world import *
from ..to_do.world_dynamic_prog.grid_world import *
from ..to_do.algo_dynamic_prog.policy_evaluation import *
from ..to_do.algo_dynamic_prog.policy_iteration import *
from ..to_do.algo_dynamic_prog.value_iteration import *
import random


envLineWorld = LineWorld_DynamicProg(7)
envGridWorld = GridWorld_DynamicProg(5)


def policy_evaluation_on_line_world() -> ValueFunction:
    """
    Creates a Line World of 7 cells (leftmost and rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Evaluation Algorithm in order to find the Value Function of a uniform random policy
    Returns the Value function (V(s)) of this policy
    """
    # TODO
    return policy_evalution(envLineWorld)
    pass




def policy_iteration_on_line_world() -> PolicyAndValueFunction:
    """
    Creates a Line World of 7 cells (leftmost and rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO
    return policy_iteration(envLineWorld)

    pass




def value_iteration_on_line_world() -> PolicyAndValueFunction:
    """
    Creates a Line World of 7 cells (leftmost and rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO
    return value_iteration(envLineWorld)

    pass




def policy_evaluation_on_grid_world() -> ValueFunction:
    """
    Creates a Grid World of 5x5 cells (upper rightmost and lower rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Evaluation Algorithm in order to find the Value Function of a uniform random policy
    Returns the Value function (V(s)) of this policy
    """
    # TODO
    return policy_evalution(envGridWorld)

    pass


def policy_iteration_on_grid_world() -> PolicyAndValueFunction:
    """
    Creates a Grid World of 5x5 cells (upper rightmost and lower rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO
    return policy_iteration(envGridWorld)
    pass


def value_iteration_on_grid_world() -> PolicyAndValueFunction:
    """
    Creates a Grid World of 5x5 cells (upper rightmost and lower rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO
    return value_iteration(envGridWorld)
    pass


def policy_evaluation_on_secret_env1() -> ValueFunction:
    """
    Creates a Secret Env1
    Launches a Policy Evaluation Algorithm in order to find the Value Function of a uniform random policy
    Returns the Value function (V(s)) of this policy
    """

    #LE CODE N'EST PAS FACTORISE PARCE QUE NOTRE P EST UN TABLEAU TANDIS QUE LE P DU ENV SECRET EST un FLOAAAATTT env.transition_probability(s, a, s_p, r_idx)
    # TODO

    env = Env1()
    States_Secret1 = env.states()
    Actions_Secret1 = env.actions()
    Rewards_Secret1 = env.rewards()
    #P_Secret1 = env.transition_probability()

    # La stratégie/policy
    pi = np.zeros((len(States_Secret1), len(Actions_Secret1)))
    for s in States_Secret1:
        pi[s, random.randint(0, len(Actions_Secret1) - 1)] = 1.0

    # La value function
    V = np.zeros((len(States_Secret1),))

    theta = 0.0001
    gamma = 0.9999

    while True:
        delta = 0
        for s in States_Secret1:
            v = V[s]
            V[s] = 0
            # boucle sur les actions
            for a in Actions_Secret1:
                # boucle sur les états suivants possible
                for s_p in States_Secret1:
                    # boucle sur les rewards
                    for r_idx, r in enumerate(Rewards_Secret1):
                        V[s] += pi[s, a] * env.transition_probability(s, a, s_p, r_idx) * (r + gamma * V[s_p])

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break

    # print(V)

    return V

    pass



def policy_iteration_on_secret_env1() -> PolicyAndValueFunction:
    """
    Creates a Secret Env1
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    env = Env1()
    States_Secret1 = env.states()
    Actions_Secret1 = env.actions()
    Rewards_Secret1 = env.rewards()


    # TODO
    # La stratégie/policy
    pi = np.zeros((len(States_Secret1), len(Actions_Secret1)))
    for s in States_Secret1:
        pi[s, random.randint(0, len(Actions_Secret1) - 1)] = 1.0

    # La value function
    V = np.zeros((len(States_Secret1),))

    while True:
        # 2 : Policy Evaluation

        theta = 0.000001
        gamma = 0.99999

        while True:
            delta = 0
            for s in States_Secret1:
                v = V[s]
                V[s] = 0
                for a in Actions_Secret1:
                    for s_p in States_Secret1:
                        for r_idx, r in enumerate(Rewards_Secret1):
                            V[s] += pi[s, a] * env.transition_probability(s, a, s_p, r_idx) * (r + gamma * V[s_p])
                delta = max(delta, abs(v - V[s]))

            if delta < theta:
                break

        # 3 : Policy Improvement
        policy_stable = True
        for s in States_Secret1:
            old_state_policy = np.copy(pi[s, :])

            best_a = -1
            best_a_score = None

            for a in Actions_Secret1:
                a_score = 0.0
                for s_p in States_Secret1:
                    for r_idx, r in enumerate(Rewards_Secret1):

                        a_score += env.transition_probability(s, a, s_p, r_idx) * (r + gamma * V[s_p])
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

    pass


def value_iteration_on_secret_env1() -> PolicyAndValueFunction:
    """
    Creates a Secret Env1
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Prints the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    env = Env1()
    States_Secret1 = env.states()
    Actions_Secret1 = env.actions()
    Rewards_Secret1 = env.rewards()

    # TODO
    V = np.zeros((len(States_Secret1),))

    theta = 0.0001
    gamma = 0.9999
    while True:
        delta = 0
        for s in States_Secret1:
            v = V[s]
            V[s] = 0
            max_cumul_A = 0
            for a in Actions_Secret1:
                cumul_A = 0
                for s_p in States_Secret1:
                    for r_idx, r in enumerate(Rewards_Secret1):
                        cumul_A += env.transition_probability(s, a, s_p, r_idx) * (r + gamma * V[s_p])

                if cumul_A > max_cumul_A:
                    max_cumul_A = cumul_A

            V[s] = max_cumul_A

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break

    # ----------------------------------------OUTPUT A DETERMINITSI POLICY----------------------------------------
    # ----------------------------------------OUTPUT A DETERMINITSI POLICY----------------------------------------

    pi = np.zeros((len(States_Secret1), len(Actions_Secret1)))

    for s in States_Secret1:
        best_a = -1
        best_a_score = None

        for a in Actions_Secret1:
            a_score = 0.0
            for s_p in States_Secret1:
                for r_idx, r in enumerate(Rewards_Secret1):
                    a_score += env.transition_probability(s, a, s_p, r_idx) * (r + gamma * V[s_p])
            if best_a_score is None or best_a_score < a_score:
                best_a = a
                best_a_score = a_score
        pi[s, :] = 0.0
        pi[s, best_a] = 1.0

    return pi, V


pass



def demo():
    print("Policy_evaluation_on_line_world")
    print(policy_evaluation_on_line_world())
    print("\n")
    print("Policy_iteration_on_line_world")
    print(policy_iteration_on_line_world())
    print("\n")
    print("Value_iteration_on_line_world")
    print(value_iteration_on_line_world())
    print("\n")


    print("Policy_evaluation_on_grid_world")
    print(policy_evaluation_on_grid_world())
    print("\n")
    print("Policy_iteration_on_grid_world")
    print(policy_iteration_on_grid_world())
    print("\n")
    print("Value_iteration_on_grid_world")
    print(value_iteration_on_grid_world())
    print("\n")

    print("policy_evaluation_on_secret_env1")
    print(policy_evaluation_on_secret_env1())
    print("\n")
    print("policy_iteration_on_secret_env1")
    print(policy_iteration_on_secret_env1())
    print("\n")
    print("value_iteration_on_secret_env1")
    print(value_iteration_on_secret_env1())
    print("\n")


