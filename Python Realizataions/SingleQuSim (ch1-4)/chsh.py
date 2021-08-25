
import random
from typing import Tuple, Callable


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

