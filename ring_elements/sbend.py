from ielement import IElement
import numpy as np


class Sbend(IElement):
    def calc_M(self, L, angle):
        R0 = L / angle
        M = np.matrix(
            [
                [np.cos(angle), R0*np.sin(angle), 0, 0, R0*(1 - np.cos(angle))],
                [-np.sin(angle)/R0, np.cos(angle), 0, 0, np.sin(angle)],
                [0, 0, 1, angle*R0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]
            ]
        )

    def calc_b(self):
        pass
