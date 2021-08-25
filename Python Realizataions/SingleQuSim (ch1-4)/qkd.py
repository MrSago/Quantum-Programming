
from interface import Qubit


def prepare_classical_message(bit: bool, q: Qubit) -> None:
    if bit:
        q.x()


def eve_measure(q: Qubit) -> bool:
    return q.measure()


def prepare_classical_message_plusminus(bit: bool, q: Qubit) -> None:
    if bit:
        q.x()
    q.h()


def eve_measure_plusminus(q: Qubit) -> bool:
    q.h()
    return q.measure()

