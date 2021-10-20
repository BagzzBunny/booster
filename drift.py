from ielement import IElement
import numpy as np


class Drift(IElement):

    def calc_M(self, L):
        M = np.matrix([[1, L, 0, 0, 0], 
                       [0, 1, 0, 0, 0],
                       [0, 0, 1, L, 0],
                       [0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1]])
        return M

    def calc_b(self, L, phi, psi):
        b = np.array([0.5*L*phi],
                      [phi],
                      [0.5*L*psi]
                      [psi],
                      [0])
        return b