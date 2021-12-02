with open("input02.txt") as f:
    counter = 0
    sequence = [int(x) for x in f.read().split("\n")]

    for position01, position02, position03, position04 in zip(
        sequence, sequence[1:], sequence[2:], sequence[3:]
    ):
        if (position01 + position02 + position03) < (
            position02 + position03 + position04
        ):
            counter += 1
    print(counter)
