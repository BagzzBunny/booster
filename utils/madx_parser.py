from cpymad.madx import Madx
from pathlib import Path
import pandas as pd
import os


class Parser():
    @classmethod
    def generate_ring_data(cls, file):
        madx = Madx()
        try:
            madx.call(file)
        except Exception:
            print(Exception)
        
    @classmethod
    def create_teable(cls):
        path_of_ring_data = os.path.abspath('Ring-data.txt')
        path = Path(path_of_ring_data)
        path2 = path.with_suffix('.csv')

        with open(path, 'r') as file1:
            with open(path2, 'w') as file2:
                for line in file1.readlines():
                    if line.startswith("@"):
                        continue
                    if line.startswith("* ") or line.startswith("$ "):
                        line = line[2:]
                    print(','.join(line.split()), file=file2, end="\n")
        
        d = pd.read_csv(path2)[1:].reset_index(drop=True)
        d
