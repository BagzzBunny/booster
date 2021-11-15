from .ielement import IElement
import numpy as np


class Sbend(IElement):

    def __init__(self, row):
        self.L = float(row['L'])
        self.angle = float(row['ANGLE'])

    def calc_M(self):
        r0 = self.L / self.angle
        m = np.matrix(
            [
                [np.cos(self.angle), r0*np.sin(self.angle), 0, 0, r0*(1 - np.cos(self.angle))],
                [-np.sin(self.angle)/r0, np.cos(self.angle), 0, 0, np.sin(self.angle)],
                [0, 0, 1, self.angle*r0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]
            ]
        )
        return m

    def calc_b(self):
        b = np.matrix([0, 0, 0, 0, 0])
        return b.T
