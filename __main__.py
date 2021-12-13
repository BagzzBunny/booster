from utils.madx_parser import Parser
from utils.solver import Solver
from utils.table_creator import TableCreator as td
import csv
import numpy as np
import matplotlib.pyplot as plt
from cpymad.madx import Madx


def generate_ring_data_table():
    #    madx = Madx(command_log="log.madx")
    #    madx.call('madx_files_folder/Boo_Seq_bpm_steer/main.madx')
    Parser.generate_ring_data("booster.madx")
    Parser.create_teable()

# generate_ring_data_table()

x_0 = []
y_0 = []

samples = np.random.multivariate_normal([0, 0], [[0.001, 0],[0, 0.001]], 1000)
for element in samples:
    x_0.append(float(element[0]))
    y_0.append(float(element[1]))

x_mean = np.mean(x_0)
y_mean = np.mean(y_0)

plt.scatter(x_0, y_0, c='b', marker='x', label='заряженная частица')
plt.scatter(x_mean, y_mean, c='r', marker='o', label='центр масс')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

solver = Solver()
x0 = np.matrix([x_mean, 0, y_mean, 0, 0])
print(x0)



x0 = x0.T
trajectory = solver.solve(x0)
x = []
y = []
for element in trajectory:
    x.append(float(element[0]))
    y.append(float(element[2]))

plt.plot(x, y, label='траектория пучка')
plt.plot(x[0], y[0], c='r', marker='o', label='начальная точка расчета')
plt.plot(x[len(x)-1], y[len(y)-1], c='r', marker='x', label='конечная точка расчета')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

# td.create_table_for_trajectory(trajectory, "trajectory.csv")
