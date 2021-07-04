import numpy as np


class ContratMDP:

    def get_actions(self) -> np.ndarray:
        pass

    def get_reward(self) -> np.ndarray:
        pass

    def get_oneValueOf_p(self, s: int, a: int, s_p: int, r_idx: int) -> int:
        pass
