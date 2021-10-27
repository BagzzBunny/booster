from ielement import IElement
import numpy as np


class QuadrupoleD(IElement):
    def calc_M(self, L, K):
        l_root_k = L*np.sqrt(K)
        M = np.matrix(
            [
                [np.cosh(l_root_k), np.sinh(l_root_k)/np.sqrt(K), 0, 0, 0],
                [np.sqrt(K)*np.sinh(l_root_k), np.cosh(l_root_k), 0, 0, 0],
                [0, 0, np.cos(l_root_k), np.sin(l_root_k)/np.sqrt(K), 0],
                [0, 0, -np.sqrt(K)*np.sin(l_root_k), np.cos(l_root_k), 0],                
                [0, 0, 0, 0, 1]
            ]
        )
        return M