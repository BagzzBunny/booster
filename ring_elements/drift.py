from .ielement import IElement
import numpy as np

#also sextuple
class Drift(IElement):
    @classmethod
    def calc_M(cls, L):
        m = np.matrix(
            [
                [1, L, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, L, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ]
        )
        return m

    @classmethod
    def calc_b(cls):
        b = np.array([0, 0, 0, 0, 0])
        return b.T

    @classmethod
    def calc_dynamics(cls, **kwargs):
        m = cls.calc_M(kwargs['L'])
        b = cls.calc_b()
        return m, b
