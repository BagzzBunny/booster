from utils.madx_parser import Parser
from utils.solver import Solver
from utils.table_creator import TableCreator as td
import csv
import numpy as np


def generate_ring_data_table():
    Parser.generate_ring_data('madx_files_folder\\Boo_Seq_bpm_steer\\main.madx')
#    Parser.create_teable()


generate_ring_data_table()

solver = Solver()  
x0 = np.matrix([1, 1, 1, 1, 1])
x0 = x0.T
#trajectory = solver.solve(x0)
#td.create_table_for_trajectory(trajectory, "trajectory.csv")
