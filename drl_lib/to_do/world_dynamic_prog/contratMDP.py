import numpy as np


#IL RESTE LE RENVOI DU s MAIS IL FAUT AVOIR LE MEME TYPE
# -> Dans LineWorld le s est un numpy.ndarray
# -> Dans GridWorld le s est un range
class ContratMDP:

    def get_actions(self) -> np.ndarray:
        pass

    def get_reward(self) -> np.ndarray:
        pass

    def get_oneValueOf_p(self, s: int, a: int, s_p: int, r_idx: int) -> int:
        pass
