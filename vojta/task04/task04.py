with open("input04.txt") as f:
    sequence = [line.split(" ") for line in f.read().split("\n")]
    positions = {"forward": 0, "depth": 0, "aim": 0}

    for command, unit in sequence:
        if command == "forward":
            positions["depth"] += positions["aim"] * int(unit)
            positions[command] += int(unit)
        elif command == "up":
            positions["aim"] -= int(unit)
        else:
            positions["aim"] += int(unit)

    print(f"{positions['forward'] * positions['depth']}")
