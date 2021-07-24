from __future__ import absolute_import
import turtle
from tkinter import *
import drl_lib.to_do.dynamic_programming as dynamic_programming
import drl_lib.to_do.monte_carlo_methods as monte_carlo_methods
import drl_lib.to_do.temporal_difference_learning as temporal_difference_learning
import drl_lib.to_do.deep_reinforcement_learning as deep_reinforcement_learning
import drl_lib.to_do.policy_gradient_methods as policy_gradient_methods

from drl_lib.to_do.algo_monte_carlo_PART1.on_policy_first_visit_monte_carlo_control import \
    on_policy_first_visit_monte_carlo_control
from drl_lib.to_do.algo_temporal_diff_lear_PART1.expected_sarsa import expected_sarsa
from drl_lib.to_do.algo_temporal_diff_lear_PART1.q_learning_offPolicy import q_learning
from drl_lib.to_do.world_monteCarlo_and_temporalDiff_PART1.TicTacToe import TicTacToe



if __name__ == "__main__":

    print("DYNAMIC PROGRAMMING")
    dynamic_programming.demo()
    print("MONTE CARLO")
    monte_carlo_methods.demo()
    """
    print("TEMPORAL DIFFERECE")
    temporal_difference_learning.demo()
    print("DEEP REINFORCEMENT LEARNING")
    deep_reinforcement_learning.demo()
    print("POLICY GRADIENT METHODS")
    policy_gradient_methods.demo()

    """






    """
    ticTacToe = TicTacToe(60,2) #2 est notre premiere cas
    result2 = on_policy_first_visit_monte_carlo_control(ticTacToe, 1.0, 0.9, 10000)
    print(result2.pi)
    print(result2.q)

    result = q_learning(ticTacToe, 0.1, 1.0, 0.9, 10000)
    print(result.pi)
    print(result.q)
    """




