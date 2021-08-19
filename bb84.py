
from simulator import SingleQubitSimulator
from interface import QuantumDevice, Qubit
from typing import List


def sample_random_bit(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        result = q.measure()
        q.reset()
    return result


def prepare_message_qubit(message: bool, basis: bool, q: Qubit) -> None:
    if message:
        q.x()
    if basis:
        q.h()


def measure_message_qubit(basis: bool, q: Qubit) -> bool:
    if basis:
        q.h()
    result = q.measure()
    q.reset()
    return result


def convert_to_hex(bits: List[bool]) -> str:
    return hex(int(
        "".join(["1" if bit else "0" for bit in bits]),
        2
    ))


def send_single_bit_with_bb84(
    your_device: QuantumDevice,
    eve_device: QuantumDevice
) -> tuple:
    [your_message, your_basis] = [
        sample_random_bit(your_device) for _ in range(2)
    ]

    eve_basis = sample_random_bit(eve_device)

    with your_device.using_qubit() as q:
        prepare_message_qubit(your_message, your_basis, q)
        eve_result = measure_message_qubit(eve_basis, q)

    return ((your_message, your_basis), (eve_result, eve_basis))


def simulate_bb84(n_bits: int) -> tuple:
    your_device = SingleQubitSimulator()
    eve_device = SingleQubitSimulator()

    key = []
    n_rounds = 0

    while len(key) < n_bits:
        n_rounds += 1
        ((your_message, your_basis), (eve_result, eve_basis)
         ) = send_single_bit_with_bb84(your_device, eve_device)

        if your_basis == eve_basis:
            assert your_message == eve_result
            key.append(your_message)

    print(
        f"Потребовалось {n_rounds} раундов, чтобы сгенерировать {n_bits}-битовый ключ.")

    return key


def apply_one_time_pad(message: List[bool], key: List[bool]) -> List[bool]:
    return [
        message_bit ^ key_bit
        for (message_bit, key_bit) in zip(message, key)
    ]

