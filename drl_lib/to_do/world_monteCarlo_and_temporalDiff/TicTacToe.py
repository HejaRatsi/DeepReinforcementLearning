import numpy as np
from drl_lib.to_do.world_monteCarlo_and_temporalDiff.contratSingleAgentEnv import SingleAgentEnv


class TicTacToe(SingleAgentEnv):


    def __init__(self, max_steps: int):
        self.cell_count = 9
        self.agent_pos = -1
        self.game_over = False
        self.current_score = 0.0
        self.max_steps = max_steps
        self.current_step = 0
        self.grid = np.arrage(self.cell_count) #grid[0] = 1 si j'y suis, grid[0] = 2 si l'autre y est et grid[0] = 0 si personne
        self.reset()
    """

    def check_winner(mark:int):
    return(((self.grid[0]==mark and self.grid[1]== mark) and self.grid[2]==mark )or #for row1

            ((self.grid[3]==mark and self.grid[4]==mark) and self.grid[5]==mark )or #for row2

            (self.grid[6]==mark and self.grid[7]==mark and self.grid[8]==mark )or #for row3

            (self.grid[0]==mark and self.grid[3]==mark and self.grid[6]== mark )or#for Colm1

            (self.grid[1]==mark and self.grid[4]==mark and self.grid[7]==mark )or #for Colm 2

            (self.grid[2]==mark and self.grid[5]==mark and self.grid[8]==mark )or #for colm 3

            (self.grid[0]==mark and self.grid[4]==mark and self.grid[8]==mark )or #daignole 1

            (self.grid[2]==mark and self.grid[4]==mark and self.grid[6]==mark )) #daignole 2
    """

    def state_id(self) -> int:
        return self.agent_pos

    def is_game_over(self) -> bool:
        return self.game_over


    def act_with_action_id(self, action_id: int):
        assert (not self.game_over)
        assert (action_id >= 0 or action_id <= 8)

        if self.grid[action_id] == 0:
            # personne donc je peux placer
            # je met à jour self.grid
            self.grid[action_id] = 1
            # je met a jour agent pos à la dernirèe position
            self.agent_pos = action_id
            #je vérifie si je gagne (game_over,current_score)
            if(check_winner(1)):
                self.game_over = True
                self.current_score = 1

        #JOUEUR ADEVERSE
        number = np.random.randint(9)
        if self.grid[action_id] == 0:
            # personne donc je peux placer
            # je met à jour self.grid
            self.grid[action_id] = 2
            # je met a jour agent pos à la dernirèe position
            self.agent_pos = action_id
            #je vérifie si il gagne (game_over,current_score)
            if (check_winner(2)):
                self.game_over = True
                self.current_score = -1

        self.current_step += 1
        if self.current_step >= self.max_steps:
            self.game_over = True


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
