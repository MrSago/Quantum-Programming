
import numpy as np
import qutip as qt

from qutip.qobj import Qobj


# Ex 5.1
ket0 = qt.Qobj([
    [1], [0]
])
ket1 = qt.Qobj([
    [0], [1]
])
ket_plus = Qobj((ket0 + ket1) / np.sqrt(2))
ket_minus = Qobj((ket0 - ket1) / np.sqrt(2))


# Ex 5.2
# ket10 = qt.tensor([qt.basis(2, label) for label in (1, 0)])
# ket001 = qt.tensor([qt.basis(2, label) for label in (0, 0, 1)])

# Ex 5.3
# zero_case = qt.Qobj([
#     [0.5],
#     [0.0],
#     [0.5],
#     [0.0]
# ]).unit()
# print(qt.tensor(ket_plus, ket0))
# print(zero_case)

# one_case = qt.Qobj([
#     [0.0],
#     [0.5],
#     [0.0],
#     [0.5]
# ]).unit()
# print(one_case)
# print(qt.tensor(ket_plus, ket1))

