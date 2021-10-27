from ring_elements.drift import Drift
from ring_elements.quadrupole_d import QuadrupoleD as qd
from ring_elements.quadrupole_f import QuadrupoleF as qf
from ring_elements.corrector import Corrector as corr
from ring_elements.sbend import Sbend
from madx_parser import Parser
import sys
import csv


#Parser.generate_ring_data('booster.madx')
#Parser.create_teable()
ring_elements = {
    'DRIFT': Drift.calc_dynamics,
    'QD': qd.calc_dynamics,
    'QF': qf.calc_dynamics,
    'KICKER': corr.calc_dynamics,
    'SBEND': Sbend.calc_dynamics,
    'SEXTUPOLE': Drift.calc_dynamics
}
with open ('Ring-data.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        kwargs = {
            'L': row['L'],
            
        }
        if row['KEYWORD'] == 'QUADRUPOLE':
            ring_elements(L)