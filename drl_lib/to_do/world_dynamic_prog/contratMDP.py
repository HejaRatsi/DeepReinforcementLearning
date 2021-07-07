import numpy as np


#IL RESTE LE RENVOI DU s MAIS IL FAUT AVOIR LE MEME TYPE
# -> Dans LineWorld le s est un numpy.ndarray
# -> Dans GridWorld le s est un range
class ContratMDP:


    def states(self) -> np.ndarray:
        pass

    def actions(self) -> np.ndarray:
        pass

    def rewards(self) -> np.ndarray:
        pass

    def is_state_terminal(self, s: int) -> bool:
        pass

    def transition_probability(self, s: int, a: int, s_p: int, r: float) -> float:
        pass

    def view_state(self, s: int):
        pass
