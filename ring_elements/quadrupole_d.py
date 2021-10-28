from .ielement import IElement
import numpy as np


class QuadrupoleD(IElement):
    @classmethod
    def calc_M(cls, L, K):
        l_root_k = L*np.sqrt(K)
        m = np.matrix(
            [
                [np.cosh(l_root_k), np.sinh(l_root_k)/np.sqrt(K), 0, 0, 0],
                [np.sqrt(K)*np.sinh(l_root_k), np.cosh(l_root_k), 0, 0, 0],
                [0, 0, np.cos(l_root_k), np.sin(l_root_k)/np.sqrt(K), 0],
                [0, 0, -np.sqrt(K)*np.sin(l_root_k), np.cos(l_root_k), 0],                
                [0, 0, 0, 0, 1]
            ]
        )
        return m

    @classmethod
    def calc_b(cls):
        b = np.array([0], [0], [0], [0], [0])
        return b

    @classmethod
    def calc_dynamics(cls, **kwargs):
        m = cls.calc_M(kwargs['L'], kwargs['K'])
        b = cls.calc_b()
        return m, b
