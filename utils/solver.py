from ring_elements.drift import Drift
from ring_elements.quadrupole_d import QuadrupoleD as qd
from ring_elements.quadrupole_f import QuadrupoleF as qf
from ring_elements.corrector import Corrector as corr
from ring_elements.sbend import Sbend
import numpy as np
import csv


class Solver():
    def __init__(self):
        self.ring_elements = {
            'DRIFT': Drift.calc_dynamics,
            'QD': qd.calc_dynamics,
            'QF': qf.calc_dynamics,
            'KICKER': corr.calc_dynamics,
            'SBEND': Sbend.calc_dynamics,
            'SEXTUPOLE': Drift.calc_dynamics
            }
    
    def solve(self, x):
        trajectory = []
        trajectory.append(x)
        i = 0
        x = np.matrix([0, 0, 0, 0, 0])
        with open ('Ring-data.csv', newline = '') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                if row['KEYWORD'] == 'QUADRUPOLE':
                    # кажется, что логику того, как парсить параметры того или иного элемента лучше перенести в конкретные классы элементов
                    # если логика одинаковая, сделать ее в общем предке
                    # тогда можно будет уйти от дублирования которой происходит здесь - строки 33 и 34 дублируются в 38 и 39. и не понадобится if else. 
                    m, b = self.ring_elements[row['NAME']](L = float(row['L']), K = float(row['K1L']) / float(row['L']))
                    x = m * trajectory[i] + b 
                elif row['KEYWORD'] not in self.ring_elements:
                    continue
                else:
                    m, b = self.ring_elements[row['KEYWORD']](L = float(row['L']), ANGLE = float(row['ANGLE']))
                    x = m * trajectory[i] + b
                trajectory.append(x)
                i += 1
        return trajectory