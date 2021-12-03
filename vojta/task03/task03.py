with open("input03.txt") as f:
    sequence = [line.split(" ") for line in f.read().split("\n")]
    positions = {"forward": 0, "up": 0, "down": 0}

    for command, unit in sequence:
        positions[command] += int(unit)

    print(f"{positions['forward'] * (positions['down'] - positions['up'])}")
