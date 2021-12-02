with open("input01.txt") as f:
    counter = 0
    sequence = [int(x) for x in f.read().split("\n")]

    for previous, current in zip(sequence, sequence[1:]):
        if current > previous:
            counter += 1
    print(counter)
