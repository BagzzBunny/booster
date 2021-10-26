from abc import ABC, abstractmethod, abstractproperty


class IElement(ABC):
    def calc_M(self):  # должен вернуть матрицу
        pass

    def calc_b(self):  # должен вернуть вектор
        pass
