from ring_elements.drift import Drift
from madx_parser import Parser
import sys
import csv


#Parser.generate_ring_data('booster.madx')
#Parser.create_teable()
with open ('Ring-data.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['NAME'], row['KEYWORD'], row['L'])