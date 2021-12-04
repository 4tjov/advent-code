import numpy as np
import copy


def remove_one_rows(sequence, bit_index):
    return sequence[sequence[:, bit_index] == "0"]


def remove_zero_rows(sequence, bit_index):
    return sequence[sequence[:, bit_index] == "1"]


def get_life_support(sequence, bit_index, oxygen):
    if len(sequence) == 1:
        return sequence
    if oxygen:
        if np.count_nonzero(sequence[:, bit_index] == "0") > np.count_nonzero(
            sequence[:, bit_index] == "1"
        ):
            sequence = remove_one_rows(sequence, bit_index)
        else:
            sequence = remove_zero_rows(sequence, bit_index)
    else:
        if np.count_nonzero(sequence[:, bit_index] == "0") > np.count_nonzero(
            sequence[:, bit_index] == "1"
        ):
            sequence = remove_zero_rows(sequence, bit_index)
        else:
            sequence = remove_one_rows(sequence, bit_index)
    sequence = get_life_support(sequence, bit_index + 1, oxygen)
    return sequence


with open("input06.txt") as f:
    sequence_oxygen = np.array([list(line) for line in f.read().split("\n")])
    sequence_co2 = copy.deepcopy(sequence_oxygen)

    binary_oxygen = "".join(get_life_support(sequence_oxygen, 0, True)[0].tolist())
    binary_co2 = "".join(get_life_support(sequence_oxygen, 0, False)[0].tolist())

    print(int(binary_oxygen, 2) * int(binary_co2, 2))
