import numpy as np
import ctypes


def bit_not(n, numbits):
    return (1 << numbits) - 1 - n


def hamming_weight(num: int) -> int:
    weight = 0

    while num:
        weight += 1
        num &= num - 1

    return weight


with open("input05.txt") as f:
    sequence = np.stack(
        np.array([list(line) for line in f.read().split("\n")]), axis=-1
    )
    number_of_lines_half = len(sequence[0]) / 2
    sequence = ["".join(row) for row in sequence]
    hws = [hamming_weight(int(number, 2)) for number in sequence]
    print(hws)
    gamma_rate = 0
    for hw in hws:
        gamma_rate <<= 1
        if hw > number_of_lines_half:
            gamma_rate ^= 1

    print(gamma_rate * bit_not(gamma_rate, len(hws)))
