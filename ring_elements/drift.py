from .ielement import IElement
import numpy as np

#also sextuple
class Drift(IElement):

    def __init__(self, row):
        super().__init__(row)

    def calc_M(self):
        m = np.matrix(
            [
                [1, self.L, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, self.L, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ]
        )
        return m

    def calc_b(self):
        b = np.matrix([0, 0, 0, 0, 0])
        return b.T
