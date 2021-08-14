
import numpy as np



ket0 = np.array([[1], [0]]) # |0>
ket1 = np.array([[0], [1]]) # |1>
# print(ket0)
# print(ket1)


ket_plus = (ket0 + ket1) / np.sqrt(2) # operation |+>
ket_minus = (ket0 - ket1) / np.sqrt(2) # operation |->
# print(ket_plus) # [[1/sqrt(2)], [1/sqrt(2)]]
# print(ket_minus) # [[1/sqrt(2)], [-1/sqrt(2)]]


# Adamar's operation (|0> => |+> and |1> => |->)
H = np.array([[1,  1], [1, -1]]) / np.sqrt(2)
# print(H @ ket0) # |+>
# print(H @ ket1) # |->


X = np.array([[0, 1], [1, 0]]) # operation NOT
# print(X @ ket0) # |0> => |1>
# print(X @ ket1) # |1> => |0>
# print(X @ H @ ket0) # |+> => |+>
# print(X @ H @ ket1) # |-> => ???

