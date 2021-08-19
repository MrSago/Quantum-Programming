
import numpy as np


# =====================Basic concepts=====================

ket0 = np.array([
    [1], [0]
], dtype=complex)  # |0>
ket1 = np.array([
    [0], [1]
], dtype=complex)  # |1>
# print(ket0)
# print(ket1)

ket_plus = (ket0 + ket1) / np.sqrt(2)  # operation |+>
ket_minus = (ket0 - ket1) / np.sqrt(2)  # operation |->
# print(ket_plus)  # [[1/sqrt(2)], [1/sqrt(2)]]
# print(ket_minus)  # [[1/sqrt(2)], [-1/sqrt(2)]]

# Adamar's operation (|0> => |+> and |1> => |->)
H = np.array([
    [1, 1],
    [1, -1]
], dtype=complex) / np.sqrt(2)
# print(H @ ket0)  # |+>
# print(H @ ket1)  # |->

# Operation NOT
X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)
# print(X @ ket0)  # |0> => |1>
# print(X @ ket1)  # |1> => |0>
# print(X @ H @ ket0)  # |+> => |+>
# print(X @ H @ ket1)  # |-> => ???

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

