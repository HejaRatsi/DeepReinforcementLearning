from ..do_not_touch.mdp_env_wrapper import Env1
from ..do_not_touch.result_structures import ValueFunction, PolicyAndValueFunction
from ..to_do.world_dynamic_prog_PART1.line_world import *
from ..to_do.world_dynamic_prog_PART1.grid_world import *
from ..to_do.algo_dynamic_prog_PART1.policy_evaluation import *
from ..to_do.algo_dynamic_prog_PART1.policy_iteration import *
from ..to_do.algo_dynamic_prog_PART1.value_iteration import *
import random


envLineWorld = LineWorld_DynamicProg(7)
envGridWorld = GridWorld_DynamicProg(5)
secretEnv = Env1()


def policy_evaluation_on_line_world() -> ValueFunction:
    """
    Creates a Line World of 7 cells (leftmost and rightmost are terminal, with -1 and 1 reward respectively)
    Launches a Policy Evaluation Algorithm in order to find the Value Function of a uniform random policy
    Returns the Value function (V(s)) of this policy
    """
    # TODO

    # La stratégie/policy

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

    # TODO

    return policy_evalution(secretEnv)

    pass


def policy_iteration_on_secret_env1() -> PolicyAndValueFunction:
    """
    Creates a Secret Env1
    Launches a Policy Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Returns the Policy (Pi(s,a)) and its Value Function (V(s))
    """


    return policy_iteration(secretEnv)

    pass


def value_iteration_on_secret_env1() -> PolicyAndValueFunction:
    """
    Creates a Secret Env1
    Launches a Value Iteration Algorithm in order to find the Optimal Policy and its Value Function
    Prints the Policy (Pi(s,a)) and its Value Function (V(s))
    """


    return value_iteration(secretEnv)



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


