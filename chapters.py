
from simulator import SingleQubitSimulator
from qrng import *
from qkd import *
from bb84 import *


def ch2():
    qsim = SingleQubitSimulator()

    for _ in range(10):
        random_sample = qrng(qsim)
        print(f"QRNG-генератор вернул {random_sample}.")


def ch3_1():
    qrng_simulator = SingleQubitSimulator()
    qkd_simulator = SingleQubitSimulator()

    for _ in range(5):
        key_bit = int(qrng(qrng_simulator))

        with qkd_simulator.using_qubit() as q:
            prepare_classical_message(key_bit, q)
            print(f"Вы подготовили классический бит ключа: {key_bit}")

            eve_measurement = int(eve_measure(q))
            print(f"Ева измерила классический бит ключа: {eve_measurement}")


def ch3_2():
    qrng_simulator = SingleQubitSimulator()
    qkd_simulator = SingleQubitSimulator()

    for _ in range(5):
        key_bit = int(qrng(qrng_simulator))

        with qkd_simulator.using_qubit() as q:
            prepare_classical_message_plusminus(key_bit, q)
            print(f"Вы подготовили классический бит ключа: {key_bit}")

            eve_measurement = int(eve_measure_plusminus(q))
            print(f"Ева измерила классический бит ключа: {eve_measurement}")


def ch3_3():
    qrng_simulator = SingleQubitSimulator()
    qkd_simulator = SingleQubitSimulator()

    for _ in range(5):
        key_bit = int(qrng(qrng_simulator))

        with qkd_simulator.using_qubit() as q:
            prepare_classical_message(key_bit, q)
            print(f"Вы подготовили классический бит ключа: {key_bit}")

            eve_measurement = int(eve_measure_plusminus(q))
            print(f"Ева измерила классический бит ключа: {eve_measurement}")

            assert key_bit == eve_measurement


def ch3_4():
    print(simulate_bb84(10))


def ch3_5():
    print("Генерирование 96-битового ключа путем симулирования BB84...")
    key = simulate_bb84(96)
    print(f"Получен ключ:              {convert_to_hex(key)}.")

    message = [
        1, 1, 0, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 1,
        1, 1, 0, 1, 1, 1, 0, 0,
        1, 0, 0, 1, 0, 1, 1, 0,
        1, 1, 0, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 1,
        1, 1, 0, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 1, 1, 0, 1,
        1, 1, 0, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 1,
        1, 1, 0, 1, 1, 1, 0, 0,
        1, 0, 1, 1, 1, 0, 1, 1
    ]
    print(f"Сообщение:                 {convert_to_hex(message)}.")

    encrypted_message = apply_one_time_pad(message, key)
    print(f"Зашифрованное сообщение:   {convert_to_hex(encrypted_message)}.")

    decrypted_message = apply_one_time_pad(encrypted_message, key)
    print(f"Ева расшифровала, получив: {convert_to_hex(decrypted_message)}.")

    assert message == decrypted_message

