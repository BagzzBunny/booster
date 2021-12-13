from prettytable import PrettyTable

class TableCreator():
    @classmethod
    def create_table_for_trajectory(cls, trajectory, output_file):
        pt = PrettyTable()
        pt.add_column("trajectory", ["x", "x'", "y", "y'", "z"])
        for i, element in enumerate(trajectory):
            pt.add_column(f"v_{i}", [float(element[0]), float(element[1]), float(element[2]), float(element[3]), float(element[4])])
        with open(output_file, 'w') as file:
            file.write(str(pt))
