
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager


class Qubit(metaclass=ABCMeta):
    @abstractmethod
    def h(self) -> None: pass

    @abstractmethod
    def x(self) -> None: pass

    @abstractmethod
    def measure(self) -> bool: pass

    @abstractmethod
    def reset(self) -> None: pass


class QuantumDevice(metaclass=ABCMeta):
    @abstractmethod
    def allocate_qubit(self) -> Qubit: pass

    @abstractmethod
    def deallocate_qubit(self, qubit: Qubit) -> None: pass

    @contextmanager
    def using_qubit(self):
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)

