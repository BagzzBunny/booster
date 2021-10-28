from .ielement import IElement
import numpy as np

#also sextuple
class Corrector(IElement):
    @classmethod
    def calc_M(cls, L, *args):
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
    def calc_b(cls, L, phi = 0, psi = 0):
        b = np.array([0.5 * L * phi], [phi], [0.5 * L * psi], [psi], [0])
        return b

    @classmethod
    def calc_dynamics(cls, **kwargs):
        m = cls.calc_M(kwargs['L'])
        b = cls.calc_b(kwargs['L'])
        return m, b
