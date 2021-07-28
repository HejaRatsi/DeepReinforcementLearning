from .algo_monte_carlo_PART1.monte_carlo_ES import monte_carlo_ES
from .algo_monte_carlo_PART1.off_policy_monte_carlo_control import off_policy_monte_carlo_control
from .algo_monte_carlo_PART1.on_policy_first_visit_monte_carlo_control import on_policy_first_visit_monte_carlo_control
from .world_monteCarlo_and_temporalDiff_PART1.TicTacToe import TicTacToe
from ..do_not_touch.result_structures import PolicyAndActionValueFunction
from ..do_not_touch.single_agent_env_wrapper import Env2


#max_steps: int, firstCase: int
ticTacToe = TicTacToe(60,2)

def monte_carlo_es_on_tic_tac_toe_solo() -> PolicyAndActionValueFunction:
    """
    Creates a TicTacToe Solo environment (Single player versus Uniform Random Opponent)
    Launches a Monte Carlo ES (Exploring Starts) in order to find the optimal Policy and its action-value function
    Returns the Optimal Policy (Pi(s,a)) and its Action-Value function (Q(s,a))
    """
    # TODO
    return monte_carlo_ES(ticTacToe, 0.1, 0.99999, 10000)

    pass


def on_policy_first_visit_monte_carlo_control_on_tic_tac_toe_solo() -> PolicyAndActionValueFunction:
    """
    Creates a TicTacToe Solo environment (Single player versus Uniform Random Opponent)
    Launches an On Policy First Visit Monte Carlo Control algorithm in order to find the optimal epsilon-greedy Policy
    and its action-value function
    Returns the Optimal epsilon-greedy Policy (Pi(s,a)) and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    # TODO
    return on_policy_first_visit_monte_carlo_control(ticTacToe, 0.1, 0.99999, 10000)

    pass


def off_policy_monte_carlo_control_on_tic_tac_toe_solo() -> PolicyAndActionValueFunction:
    """
    Creates a TicTacToe Solo environment (Single player versus Uniform Random Opponent)
    Launches an Off Policy Monte Carlo Control algorithm in order to find the optimal greedy Policy and its action-value function
    Returns the Optimal Policy (Pi(s,a)) and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    # TODO
    return off_policy_monte_carlo_control(ticTacToe, 0.1, 0.99999, 10000)

    pass


def monte_carlo_es_on_secret_env2() -> PolicyAndActionValueFunction:
    """
    Creates a Secret Env2
    Launches a Monte Carlo ES (Exploring Starts) in order to find the optimal Policy and its action-value function
    Returns the Optimal Policy (Pi(s,a)) and its Action-Value function (Q(s,a))
    """
    env = Env2()
    return monte_carlo_ES(env, 0.1, 0.99999, 10000)
    # TODO
    pass


def on_policy_first_visit_monte_carlo_control_on_secret_env2() -> PolicyAndActionValueFunction:
    """
    Creates a Secret Env2
    Launches an On Policy First Visit Monte Carlo Control algorithm in order to find the optimal epsilon-greedy Policy and its action-value function
    Returns the Optimal epsilon-greedy Policy (Pi(s,a)) and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    env = Env2()
    return on_policy_first_visit_monte_carlo_control(env, 0.1, 0.99999, 10000)
    # TODO
    pass


def off_policy_monte_carlo_control_on_secret_env2() -> PolicyAndActionValueFunction:
    """
    Creates a Secret Env2
    Launches an Off Policy Monte Carlo Control algorithm in order to find the optimal greedy Policy and its action-value function
    Returns the Optimal Policy (Pi(s,a)) and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    env = Env2()
    return off_policy_monte_carlo_control(env, 0.1, 0.99999, 10000)
    # TODO
    pass


def demo():
    print("Monte_carlo_es_on_tic_tac_toe_solo")
    print(monte_carlo_es_on_tic_tac_toe_solo())
    print("\n")
    print("On_policy_first_visit_monte_carlo_control_on_tic_tac_toe_solo")
    print(on_policy_first_visit_monte_carlo_control_on_tic_tac_toe_solo())
    print("\n")
    print("Off_policy_monte_carlo_control_on_tic_tac_toe_solo")
    print(off_policy_monte_carlo_control_on_tic_tac_toe_solo())
    print("\n")

    print("Monte_carlo_es_on_secret_env2")
    print("\n")
    print(monte_carlo_es_on_secret_env2())
    print("On_policy_first_visit_monte_carlo_control_on_secret_env2")
    print("\n")
    print(on_policy_first_visit_monte_carlo_control_on_secret_env2())
    print("off_policy_monte_carlo_control_on_secret_env2")
    print("\n")
    print(off_policy_monte_carlo_control_on_secret_env2())
