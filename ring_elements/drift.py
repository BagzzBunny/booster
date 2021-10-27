from ielement import IElement
import numpy as np

#also sextuple
class Drift(IElement):
    def calc_M(self, L):
        M = np.matrix(
            [
                [1, L, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, L, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ]
        )
        return M
