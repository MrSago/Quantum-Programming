
from qrng import qrng
from simulator import SingleQubitSimulator


def main():
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"QRNG-генератор вернул {random_sample}.")


if __name__ == "__main__":
    main()

