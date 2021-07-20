from __future__ import absolute_import

import drl_lib.to_do.dynamic_programming as dynamic_programming
import drl_lib.to_do.monte_carlo_methods as monte_carlo_methods
import drl_lib.to_do.temporal_difference_learning as temporal_difference_learning
from drl_lib.to_do.algo_temporal_diff_lear.expected_sarsa import expected_sarsa
from drl_lib.to_do.algo_temporal_diff_lear.q_learning_offPolicy import q_learning
from drl_lib.to_do.world_monteCarlo_and_temporalDiff.TicTacToe import TicTacToe

if __name__ == "__main__":


    dynamic_programming.demo()
    monte_carlo_methods.demo()
    temporal_difference_learning.demo()


    """

    ticTacToe = TicTacToe(60)
    result2 = expected_sarsa(ticTacToe, 0.1, 1.0, 0.9, 10000)
    print(result2.pi)
    print(result2.q)
    """




