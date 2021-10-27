from abc import ABC, abstractmethod, abstractproperty


class IElement(ABC):
    @abstractmethod
    def calc_M(self):  # должен вернуть матрицу
        pass
