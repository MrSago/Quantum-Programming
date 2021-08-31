
import qutip as qt
import random
from typing import Tuple, Callable
import numpy as np

from simulator import Simulator


Strategy = Tuple[Callable[[int], int], Callable[[int], int]]


def random_bit() -> int:
    return random.randint(0, 1)


def referee(strategy: Callable[[], Strategy]) -> bool:
    you, eve = strategy()
    your_input, eve_input = random_bit(), random_bit()
    parity = 0 if you(your_input) == eve(eve_input) else 1
    return parity == (your_input and eve_input)


def est_win_probability(strategy: Callable[[], Strategy],
                        n_games: int = 1000) -> float:
    return sum(
        referee(strategy)
        for _ in range(n_games)
    ) / n_games


def constant_strategy() -> Strategy:
    return (
        lambda your_input: 0,
        lambda eve_input: 0
    )


def quantum_strategy(initial_state: qt.Qobj) -> Strategy:
    shared_system = Simulator(capacity=2)
    shared_system.register_state = initial_state

    your_qubit = shared_system.allocate_qubit()
    eve_qubit = shared_system.allocate_qubit()

    shared_system.register_state = qt.bell_state()
    your_angles = [90 * np.pi / 180, 0]
    eve_angles = [45 * np.pi / 180, 135 * np.pi / 180]

    def you(your_input: int) -> int:
        your_qubit.ry(your_angles[your_input])
        return your_qubit.measure()

    def eve(eve_input: int) -> int:
        eve_qubit.ry(eve_angles[eve_input])
        return eve_qubit.measure()

    return you, eve

