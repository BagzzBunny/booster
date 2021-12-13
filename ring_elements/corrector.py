from .ielement import IElement
import numpy as np

#also sextuple
class Corrector(IElement):

    def __init__(self, row):
        super().__init__(row)
        self.phi = 0
        self.psi = 0
    
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
        b = np.matrix([0.5 * self.L * self.phi, self.phi, 0.5 * self.L * self.psi, self.psi, 0])
        return b.T
