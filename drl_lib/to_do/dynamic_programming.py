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

    # La stratégie/policy

    pi = np.zeros((len(envLineWorld.states()), len(envLineWorld.actions())))
    for s in envLineWorld.states():
        pi[s, random.randint(0, len(envLineWorld.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(envLineWorld.states()),))

    return policy_evalution(envLineWorld,pi,V)
    pass




def policy_iteration_on_line_world() -> PolicyAndValueFunction:
    """
    Creates a Line World of 7 cells (leftmost and rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO

    # La stratégie/policy
    pi = np.zeros((len(envLineWorld.states()), len(envLineWorld.actions())))
    for s in envLineWorld.states():
        pi[s, random.randint(0, len(envLineWorld.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(envLineWorld.states()),))

    return policy_iteration(envLineWorld,pi,V)

    pass




def value_iteration_on_line_world() -> PolicyAndValueFunction:
    """
    Creates a Line World of 7 cells (leftmost and rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO


    # La value function
    V = np.zeros((len(envLineWorld.states()),))
    return value_iteration(envLineWorld,V)

    pass




def policy_evaluation_on_grid_world() -> ValueFunction:
    """
    Creates a Grid World of 5x5 cells (upper rightmost and lower rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Evaluation Algorithm in order to find the Value Function of a uniform random policy
    Returns the Value function (V(s)) of this policy
    """
    # TODO

    # La stratégie/policy
    pi = np.zeros((len(envGridWorld.states()), len(envGridWorld.actions())))
    for s in envGridWorld.states():
        pi[s, random.randint(0, len(envGridWorld.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(envGridWorld.states()),))

    return policy_evalution(envGridWorld,pi,V)

    pass


def policy_iteration_on_grid_world() -> PolicyAndValueFunction:
    """
    Creates a Grid World of 5x5 cells (upper rightmost and lower rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO

    # La stratégie/policy
    pi = np.zeros((len(envGridWorld.states()), len(envGridWorld.actions())))
    for s in envGridWorld.states():
        pi[s, random.randint(0, len(envGridWorld.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(envGridWorld.states()),))

    return policy_iteration(envGridWorld,pi,V)
    pass


def value_iteration_on_grid_world() -> PolicyAndValueFunction:
    """
    Creates a Grid World of 5x5 cells (upper rightmost and lower rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    # TODO

    # La value function
    V = np.zeros((len(envGridWorld.states()),))
    return value_iteration(envGridWorld,V)
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
    # La stratégie/policy
    pi = np.zeros((len(env.states()), len(env.actions())))
    for s in env.states():
        pi[s, random.randint(0, len(env.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(env.states()),))

    return policy_evalution(env, pi, V)

    pass


def policy_iteration_on_secret_env1() -> PolicyAndValueFunction:
    """
    Creates a Secret Env1
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """
    env = Env1()
    # La stratégie/policy
    pi = np.zeros((len(env.states()), len(env.actions())))
    for s in env.states():
        pi[s, random.randint(0, len(env.actions()) - 1)] = 1.0

    # La value function
    V = np.zeros((len(env.states()),))

    return policy_iteration(env, pi, V)

    pass


def value_iteration_on_secret_env1() -> PolicyAndValueFunction:
    """
    Creates a Secret Env1
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Prints the Policy (Pi(s,a)) and its Value Function (V(s))
    """

    env = Env1()

    # La value function
    V = np.zeros((len(env.states()),))

    return value_iteration(env,V)



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


