from utils.madx_parser import Parser
from utils.solver import Solver
import csv
import numpy as np


def generate_ring_data_table():
    Parser.generate_ring_data('booster.madx')
    Parser.create_teable()


#generate_ring_data_table()

solver = Solver()  
x0 = np.matrix([0, 1, 0, 1, 0])
x0 = x0.T
trajectory = solver.solve(x0)
print(trajectory)
