from abc import ABC, abstractmethod


class IElement(ABC):

    def __init__(self, row):
        self.L = float(row['L'])

    @abstractmethod
    def calc_M(self):  # должен вернуть матрицу
        pass

    @abstractmethod
    def calc_b(self):
        pass
