from ring_elements.drift import Drift
from ring_elements.quadrupole import Quadrupole
from ring_elements.corrector import Corrector as corr
from ring_elements.sbend import Sbend
import numpy as np
import csv


class Solver():
    def __init__(self):
        self.ring_elements = {
            'DRIFT': Drift,
            'QUADRUPOLE': Quadrupole,
            'KICKER': corr,
            'SBEND': Sbend,
            'SEXTUPOLE': Drift
            }

    def make_element(self, row):
        if row['KEYWORD'] in self.ring_elements:
            element = self.ring_elements[row['KEYWORD']](row)
            return element
        return None
    
    def solve(self, x):
        trajectory = [x]
        i = 0
        with open ('Ring-data.csv', newline = '') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                element = self.make_element(row)
                if element is None:
                    continue
                else:
                    m = element.calc_M()
                    b = element.calc_b()
                    x = m * trajectory[i] + b
                    trajectory.append(x)
                i += 1
        return trajectory
