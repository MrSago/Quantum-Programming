
from functools import partial
from chsh import *


def ch5() -> None:
    constant_pr = est_win_probability(constant_strategy, 100)
    print(f"Классическая стратегия: {constant_pr:0.1%}")

    initial_state = qt.Qobj([[1], [0], [0], [1]]) / np.sqrt(2)
    quantum_pr = est_win_probability(
        partial(quantum_strategy, initial_state),
        100
    )
    print(f"Квантовая стратегия {quantum_pr:0.1%}\n"
          f"состояние описывается:\n{initial_state}")

