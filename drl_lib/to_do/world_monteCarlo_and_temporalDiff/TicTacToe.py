import numpy as np
from drl_lib.to_do.world_monteCarlo_and_temporalDiff.contratSingleAgentEnv import SingleAgentEnv


class TicTacToe(SingleAgentEnv):


    def __init__(self, max_steps: int):
        self.cell_count = 9
        self.agent_pos = 0
        self.game_over = False
        self.current_score = 0.0
        self.max_steps = max_steps
        self.current_step = 0
        self.reset()



    # implémenter les fonctions ci-dessous
    def state_id(self) -> int:
        pass

    def is_game_over(self) -> bool:
        pass

    def act_with_action_id(self, action_id: int):
        pass

    def score(self) -> float:
        pass

    def available_actions_ids(self) -> np.ndarray:
        pass

    def reset(self):
        pass

    def view(self):
        pass

    def reset_random(self):
        pass
