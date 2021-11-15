from .ielement import IElement
import numpy as np


class Quadrupole(IElement):

    def __init__(self, row):
        self.L = float(row['L'])
        self.K = float(row['K1L']) / float(row['L'])

    def calc_M(self):
        if self.K < 0:
            self.K = np.absolute(self.K)
            l_root_k = self.L*np.sqrt(self.K)
            m = np.matrix(
                [
                    [np.cosh(l_root_k), np.sinh(l_root_k)/np.sqrt(self.K), 0, 0, 0],
                    [np.sqrt(self.K)*np.sinh(l_root_k), np.cosh(l_root_k), 0, 0, 0],
                    [0, 0, np.cos(l_root_k), np.sin(l_root_k)/np.sqrt(self.K), 0],
                    [0, 0, -np.sqrt(self.K)*np.sin(l_root_k), np.cos(l_root_k), 0],                
                    [0, 0, 0, 0, 1]
                ]
            )
            return m
        else:
            l_root_k = self.L*np.sqrt(self.K)
            m = np.matrix(
                [
                    [np.cos(l_root_k), np.sin(l_root_k)/np.sqrt(self.K), 0, 0, 0],
                    [-np.sqrt(self.K)*np.sin(l_root_k), np.cos(l_root_k), 0, 0, 0],
                    [0, 0, np.cosh(l_root_k), np.sinh(l_root_k)/np.sqrt(self.K), 0],
                    [0, 0, np.sqrt(self.K)*np.sinh(l_root_k), np.cosh(l_root_k), 0],
                    [0, 0, 0, 0, 1]
                ]
            )
            return m

    def calc_b(self):
        b = np.matrix([0, 0, 0, 0, 0])
        return b.T
