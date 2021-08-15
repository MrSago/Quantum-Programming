
from simulator import SingleQubitSimulator
from qrng import *
from qkd import *


def ch2():
    qsim = SingleQubitSimulator()
    for i in range(10):
        random_sample = qrng(qsim)
        print(f"QRNG-генератор вернул {random_sample}.")

def ch3():
    qrng_simulator = SingleQubitSimulator()
    qkd_simulator = SingleQubitSimulator()
    for i in range(5):
        key_bit = int(qrng(qrng_simulator))
        with qkd_simulator.using_qubit() as q:
            prepare_classical_message(key_bit, q)
            print(f"Вы подготовили классический бит ключа: {key_bit}")
            eve_measurement = int(eve_measure(q))
            print(f"Ева измерила классический бит ключа: {eve_measurement}")

