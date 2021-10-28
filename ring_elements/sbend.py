from .ielement import IElement
import numpy as np


class Sbend(IElement):
    @classmethod
    def calc_M(cls, L, angle):
        R0 = L / angle
        m = np.matrix(
            [
                [np.cos(angle), R0*np.sin(angle), 0, 0, R0*(1 - np.cos(angle))],
                [-np.sin(angle)/R0, np.cos(angle), 0, 0, np.sin(angle)],
                [0, 0, 1, angle*R0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]
            ]
        )
        return m

    @classmethod
    def calc_b(cls):
        b = np.array([0, 0, 0, 0, 0])
        return b.T

    @classmethod
    def calc_dynamics(cls, **kwargs):
        m = cls.calc_M(kwargs['L'], kwargs['ANGLE'])
        b = cls.calc_b()
        return m, b
