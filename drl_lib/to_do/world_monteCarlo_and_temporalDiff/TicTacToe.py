import numpy as np
from drl_lib.to_do.world_monteCarlo_and_temporalDiff.contratSingleAgentEnv import SingleAgentEnv


class TicTacToe(SingleAgentEnv):


    def __init__(self, max_steps: int):
        self.cell_count = 9
        self.all_cell = 19683 # 3 puissance 9
        self.agent_pos = 0 # à vérifier, c'est la position au début
        self.game_over = False
        self.current_score = 0.0
        self.max_steps = max_steps
        self.current_step = 0
        self.reset()



    # implémenter les fonctions ci-dessous

    def state_id(self) -> int:
        return self.agent_pos

    def is_game_over(self) -> bool:
        return self.game_over

    #NARESH
    #les actions sont les indices des cases de 0 à 8 inclus
    #tu joue après tu fais joueur le robot
    def act_with_action_id(self, action_id: int):
        pass

    def score(self) -> float:
        return self.current_score

    def available_actions_ids(self) -> np.ndarray:
        if self.game_over:
            return np.array([], dtype=np.int)
        return np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])  # Poser sur une des cases

    #NARESH
    def reset(self):
        pass


    def view(self):
        pass

    #NARESH
    def reset_random(self):
        pass
