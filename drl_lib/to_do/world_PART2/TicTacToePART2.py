from drl_lib.to_do.world_PART2.contratDeepSingleAgentWithDiscreteActionsEnv import DeepSingleAgentWithDiscreteActionsEnv
import numpy as np
import tensorflow as tf

class TicTacToePART2(DeepSingleAgentWithDiscreteActionsEnv):

    def __init__(self, max_steps: int, firstCase: int):
        self.firstCase = firstCase  # la premiere case qu'on va jouer
        self.cell_count = 9
        self.agent_pos_now = -1  # on n'en a pas besoin dans l'algo
        self.gridState = 1
        self.temp = ""
        self.game_over = False
        self.current_score = 0.0
        self.max_steps = max_steps
        self.current_step = 0
        self.grid = np.array([1, 1, 1, 1, 1, 1, 1, 1,
                              1])  # grid[0] = 1 si personne, grid[0] = 2 si j'y suis, grid[0] = 3 si l'autre y est
        # self.reset()

    def check_winner(self, mark: int):
        return ((self.grid[0] == mark and self.grid[1] == mark and self.grid[2] == mark) or  # for row1
                (self.grid[3] == mark and self.grid[4] == mark and self.grid[5] == mark) or  # for row2
                (self.grid[6] == mark and self.grid[7] == mark and self.grid[8] == mark) or  # for row3
                (self.grid[0] == mark and self.grid[3] == mark and self.grid[6] == mark) or  # for Colm1
                (self.grid[1] == mark and self.grid[4] == mark and self.grid[7] == mark) or  # for Colm 2
                (self.grid[2] == mark and self.grid[5] == mark and self.grid[8] == mark) or  # for colm 3
                (self.grid[0] == mark and self.grid[4] == mark and self.grid[8] == mark) or  # daignole 1
                (self.grid[2] == mark and self.grid[4] == mark and self.grid[6] == mark))  # daignole 2


    #PETIT SOUCIS ICI
    def state_description(self) -> np.ndarray:
        return tf.keras.utils.to_categorical(self.gridState, 19683)

    # PETIT SOUCIS ICI peut ettre ici pas sur mais la haut surrrrr
    def state_description_length(self) -> int:
        return 19683 #3 puissance 9 nombre d'états possible

    def max_actions_count(self) -> int:
        return 9

    def is_game_over(self) -> bool:
        return self.game_over

    def act_with_action_id(self, action_id: int):
        test = 0
        assert (not self.game_over)
        assert (action_id >= 0 and action_id <= 8)

        if self.grid[action_id] == 1:
            # personne donc je peux placer
            self.grid[action_id] = 2
            self.gridState = 1
            self.temp = ""
            for i in range(self.cell_count):
                self.temp += str(self.grid[i])
            self.gridState = int(self.temp)
            # je met a jour agent pos à la dernirèe position
            self.agent_pos_now = action_id
            # je vérifie si je gagne (game_over,current_score)
            if (self.check_winner(2)):
                self.game_over = True
                test = 1
                self.current_score = 1

        # JOUEUR ADVERSE
        number = np.random.randint(9)
        if self.grid[number] == 1:
            # personne donc je peux placer
            self.grid[number] = 3
            self.gridState = 1
            self.temp = ""
            for i in range(self.cell_count):
                # self.gridState *= self.grid[i]
                self.temp += str(self.grid[i])
            self.gridState = int(self.temp)
            # je vérifie si il gagne (game_over,current_score)
            if (self.check_winner(3)):
                self.game_over = True
                test = 2
                self.current_score = -1

        self.current_step += 1
        if self.current_step >= self.max_steps:
            self.game_over = True
            test = 3
        """
        if(test == 1):
            print(self.gridState)
            print(self.grid)
            print("GAME OVER because of win of player 1!!!")
        elif(test == 2):
            print(self.gridState)
            print(self.grid)
            print("GAME OVER because of win of player 2!!!")
        elif(test == 3):
            print(self.gridState)
            print(self.grid)
            print("GAME OVER because of max_steps!!!")
        """


    def score(self) -> float:
        return self.current_score

    def available_actions_ids(self) -> np.ndarray:
        if self.game_over:
            return np.array([], dtype=np.int)
        return np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])  # Poser sur une des cases

    def reset(self):
        self.gridState = 1
        self.temp = ""
        for i in range(self.cell_count):
            self.grid[i] = 1
            # self.gridState *= self.grid[i]
        self.agent_pos_now = self.firstCase
        number = np.random.randint(9)
        while (number == self.firstCase):
            number = np.random.randint(9)
        self.grid[self.agent_pos_now] = 2
        self.grid[number] = 3
        self.game_over = False
        self.current_step = 0
        self.current_score = 0.0
        for i in range(self.cell_count):
            self.temp += str(self.grid[i])
        self.gridState = int(self.temp)
