
import numpy as np
import random
from typing import Tuple, Callable
from interface import QuantumDevice
from simulator import SingleQubitSimulator


# =====================Basic concepts=====================

ket0 = np.array([
    [1], [0]
])  # |0>
ket1 = np.array([
    [0], [1]
])  # |1>
# print(ket0)
# print(ket1)


ket_plus = (ket0 + ket1) / np.sqrt(2)  # operation |+>
ket_minus = (ket0 - ket1) / np.sqrt(2)  # operation |->
# print(ket_plus)  # [[1/sqrt(2)], [1/sqrt(2)]]
# print(ket_minus)  # [[1/sqrt(2)], [-1/sqrt(2)]]


# Hadamard's operation (|0> => |+> and |1> => |->)
H = np.array([
    [1, 1],
    [1, -1]
]) / np.sqrt(2)
# print(H @ ket0)  # |+>
# print(H @ ket1)  # |->


# Operation NOT
X = np.array([
    [0, 1],
    [1, 0]
])
# print(X @ ket0)  # |0> => |1>
# print(X @ ket1)  # |1> => |0>
# print(X @ H @ ket0)  # |+> => |+>
# print(X @ H @ ket1)  # |-> => ???


I = np.array([
    [1, 0],
    [0, 1]
])
IX = np.kron(I, X)
XX = np.kron(X, X)
ket00 = np.kron(ket0, ket0)
# print(IX) # I o X
# print(XX) # X o X
# print(ket00) # |00>
# print(IX @ ket00) # |01>
# print(XX @ ket00) # |11>

# ========================================================


# Ex 3.1
# print(X @ ket0)
# print(X @ ket1)


# Ex 3.2
# print((ket_plus + ket_minus) / np.sqrt(2))


# Ex 3.3
# print(np.abs(ket_minus.conj().transpose() @ ket0) ** 2)
# print(np.abs(ket_minus.conj().transpose() @ ket1) ** 2)


# Ex 3.4
# ciphertext = [bit == '1' for bit in '10100101']
# key = [bit == '1' for bit in '00100110']
# plaintext = [cipher_bit ^ key_bit for (cipher_bit, key_bit) in zip(ciphertext, key)]
# print("".join("1" if bit else "0" for bit in plaintext))


# Ex 4.1
# Strategy = Tuple[Callable[[int], int], Callable[[int], int]]


# def random_bit(device: QuantumDevice) -> int:
#     with device.using_qubit() as q:
#         q.h()
#         return int(q.measure())


# def referee(strategy: Callable[[], Strategy]) -> bool:
#     qsim = SingleQubitSimulator()
#     you, eve = strategy()
#     your_input, eve_input = random_bit(qsim), random_bit(qsim)
#     parity = 0 if you(your_input) == eve(eve_input) else 1
#     return parity == (your_input and eve_input)


# Ex 4.2
# HI = np.kron(H, I) # H o I
# print(HI @ ket00) # |+0>

