from .algo_temporal_diff_lear_PART1.expected_sarsa import expected_sarsa
from .algo_temporal_diff_lear_PART1.q_learning_offPolicy import q_learning
from .algo_temporal_diff_lear_PART1.sarsa_onPolicy import sarsa_onPolicy
from .world_monteCarlo_and_temporalDiff_PART1.TicTacToe import TicTacToe
from ..do_not_touch.result_structures import PolicyAndActionValueFunction
from ..do_not_touch.single_agent_env_wrapper import Env3


#max_steps: int, firstCase: int
ticTacToe = TicTacToe(60,2)


def sarsa_on_tic_tac_toe_solo() -> PolicyAndActionValueFunction:
    """
    Creates a TicTacToe Solo environment (Single player versus Uniform Random Opponent)
    Launches a SARSA Algorithm in order to find the optimal epsilon-greedy Policy and its action-value function
    Returns the optimal epsilon-greedy Policy and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    # TODO
    return sarsa_onPolicy(ticTacToe, 0.1, 1.0, 0.9, 10000)

    pass


def q_learning_on_tic_tac_toe_solo() -> PolicyAndActionValueFunction:
    """
    Creates a TicTacToe Solo environment (Single player versus Uniform Random Opponent)
    Launches a Q-Learning algorithm in order to find the optimal greedy Policy and its action-value function
    Returns the optimal greedy Policy and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    # TODO
    return q_learning(ticTacToe, 0.1, 1.0, 0.9, 10000)

    pass


def expected_sarsa_on_tic_tac_toe_solo() -> PolicyAndActionValueFunction:
    """
    Creates a TicTacToe Solo environment (Single player versus Uniform Random Opponent)
    Launches a Expected SARSA Algorithm in order to find the optimal epsilon-greedy Policy and its action-value function
    Returns the optimal epsilon-greedy Policy and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    # TODO
    return expected_sarsa(ticTacToe, 0.1, 1.0, 0.9, 10000)

    pass


def sarsa_on_secret_env3() -> PolicyAndActionValueFunction:
    """
    Creates a Secret Env3
    Launches a SARSA Algorithm in order to find the optimal epsilon-greedy Policy and its action-value function
    Returns the optimal epsilon-greedy Policy and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    env = Env3()
    return sarsa_onPolicy(env, 0.1, 1.0, 0.9, 10000)
    # TODO
    pass


def q_learning_on_secret_env3() -> PolicyAndActionValueFunction:
    """
    Creates a Secret Env3
    Launches a Q-Learning algorithm in order to find the optimal greedy Policy and its action-value function
    Returns the optimal greedy Policy and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    env = Env3()
    return q_learning(env, 0.1, 1.0, 0.9, 10000)
    # TODO
    pass


def expected_sarsa_on_secret_env3() -> PolicyAndActionValueFunction:
    """
    Creates a Secret Env3
    Launches a Expected SARSA Algorithm in order to find the optimal epsilon-greedy Policy and its action-value function
    Returns the optimal epsilon-greedy Policy and its Action-Value function (Q(s,a))
    Experiment with different values of hyper parameters and choose the most appropriate combination
    """
    env = Env3()
    return expected_sarsa(env, 0.1, 1.0, 0.9, 10000)
    # TODO
    pass


def demo():
    print("Sarsa_on_tic_tac_toe_solo")
    print(sarsa_on_tic_tac_toe_solo())
    print("\n")
    print("Q_learning_on_tic_tac_toe_solo")
    print(q_learning_on_tic_tac_toe_solo())
    print("\n")
    print("Expected_sarsa_on_tic_tac_toe_solo")
    print(expected_sarsa_on_tic_tac_toe_solo())
    print("\n")

    print("Sarsa_on_secret_env3")
    print(sarsa_on_secret_env3())
    print("\n")
    print("Q_learning_on_secret_env3")
    print(q_learning_on_secret_env3())
    print("\n")
    print("Expected_sarsa_on_secret_env3")
    print(expected_sarsa_on_secret_env3())
    print("\n")
