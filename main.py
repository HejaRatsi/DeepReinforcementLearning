from __future__ import absolute_import
import turtle
from tkinter import *
import drl_lib.to_do.dynamic_programming as dynamic_programming
import drl_lib.to_do.monte_carlo_methods as monte_carlo_methods
import drl_lib.to_do.temporal_difference_learning as temporal_difference_learning
import drl_lib.to_do.deep_reinforcement_learning as deep_reinforcement_learning
import drl_lib.to_do.policy_gradient_methods as policy_gradient_methods
from drl_lib.do_not_touch.single_agent_env_wrapper import Env3, Env2
from drl_lib.to_do.algo_deep_reinfo_learning_PART2.episodic_semi_gradient_sarsa import episodic_semi_gradient_sarsa
from drl_lib.to_do.algo_monte_carlo_PART1.monte_carlo_ES import monte_carlo_ES
from drl_lib.to_do.algo_monte_carlo_PART1.off_policy_monte_carlo_control import off_policy_monte_carlo_control

from drl_lib.to_do.algo_monte_carlo_PART1.on_policy_first_visit_monte_carlo_control import \
    on_policy_first_visit_monte_carlo_control
from drl_lib.to_do.algo_temporal_diff_lear_PART1.expected_sarsa import expected_sarsa
from drl_lib.to_do.algo_temporal_diff_lear_PART1.q_learning_offPolicy import q_learning
from drl_lib.to_do.algo_temporal_diff_lear_PART1.sarsa_onPolicy import sarsa_onPolicy
from drl_lib.to_do.world_PART2.TicTacToePART2 import TicTacToePART2
from drl_lib.to_do.world_monteCarlo_and_temporalDiff_PART1.TicTacToe import TicTacToe
import numpy as np



if __name__ == "__main__":

    print("DYNAMIC PROGRAMMING")
    dynamic_programming.demo()
    print("MONTE CARLO")
    monte_carlo_methods.demo()
    print("TEMPORAL DIFFERECE")
    temporal_difference_learning.demo()
    print("DEEP REINFORCEMENT LEARNING")
    deep_reinforcement_learning.demo()
    print("POLICY GRADIENT METHODS")
    policy_gradient_methods.demo()


    """
    ticTacToe = TicTacToe(60,2) #2 est notre premiere cas
    result2 = on_policy_first_visit_monte_carlo_control(ticTacToe, 1.0, 0.9, 10000)
    print(result2.pi)
    print(result2.q)

    
    result = q_learning(ticTacToe, 0.1, 1.0, 0.9, 10000)
    print(result.pi)
    print(result.q)
    """


    """
    ticTacToe2 = TicTacToePART2(60, 2)  # 2 est notre premiere cas

    episodic_semi_gradient_sarsa(
        ticTacToe2
    )
    
    """

    """
    ticTacToe = TicTacToe(70, 2)
    env2 = Env2()
    env3 = Env3()

    result = expected_sarsa(env3, 0.1, 1.0, 0.9, 10000)

    #result = off_policy_monte_carlo_control(env2, 0.1, 0.99999, 10000)
    fichier1 = open("policy.txt", "a")
    fichier1.write(str(result.pi))
    fichier1.close()

    fichier2 = open("actionVal.txt", "a")
    fichier2.write(str(result.q))
    fichier2.close()
    
    """

