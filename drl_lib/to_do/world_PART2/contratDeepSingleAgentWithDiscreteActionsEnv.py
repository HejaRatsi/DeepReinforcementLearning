import numpy as np


class DeepSingleAgentWithDiscreteActionsEnv:
    def state_description(self) -> np.ndarray:
        pass

    def state_description_length(self) -> int:
        pass

    def max_actions_count(self) -> int:
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