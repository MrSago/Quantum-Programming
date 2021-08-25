
from interface import Qubit, QuantumDevice
import numpy as np
import qutip as qt
from qutip.qip.operations import hadamard_transform
from typing import List


class SimulatedQubit(Qubit):
    qubit_id: int
    parent: "Simulator"

    def __init__(self, parent_simulator: "Simulator", id: int):
        self.qubit_id = id
        self.parent = parent_simulator

    def h(self) -> None:
        self.parent._apply(hadamard_transform(), [self.qubit_id])

    def ry(self, angle: float) -> None:
        self.parent._apply(qt.ry(angle), [self.qubit_id])

    def x(self) -> None:
        self.parent._apply(qt.sigmax(), [self.qubit_id])

    def measure(self) -> bool:
        projectors = [
            qt.circuit.gate_expand_1toN(
                qt.basis(2, outcome) * qt.basis(2, outcome).dag(),
                self.parent.capacity,
                self.qubit_id
            )
            for outcome in (0, 1)
        ]
        post_measurement_states = [
            projector * self.parent.register_state
            for projector in projectors
        ]
        probabilities = [
            post_measurement_state.norm() ** 2
            for post_measurement_state in post_measurement_states
        ]
        sample = np.random.choice([0, 1], p=probabilities)
        self.parent.register_state = post_measurement_states[sample].unit()
        return bool(sample)

    def reset(self) -> None:
        if self.measure():
            self.x()


class Simulator(QuantumDevice):
    capacity: int
    available_qubits: List[SimulatedQubit]
    regiter_state: qt.Qobj

    def __init__(self, capacity=3):
        self.capacity = capacity
        self.available_qubits = [
            SimulatedQubit(self, i)
            for i in range(capacity)
        ]
        self.regiter_state = qt.tensor(
            *[
                qt.basis(2, 0)
                for _ in range(capacity)
            ]
        )

    def allocate_qubit(self) -> SimulatedQubit:
        if self.available_qubits:
            return self.available_qubits.pop()

    def deallocate_qubit(self, qubit: SimulatedQubit) -> None:
        self.available_qubits.append(qubit)

    def _apply(self, unitary: qt.Qobj, ids: List[int]) -> None:
        if len(ids) != 1:
            raise ValueError(
                "Поддерживаются только однокубитовые унитарные матрицы.")
        matrix = qt.circuit.gate_expand_1toN(
            unitary, self.capacity, ids[0]
        )
        self.register_state = matrix * self.register_state

