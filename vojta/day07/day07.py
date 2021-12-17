with open("input07.txt") as f:
    input = f.read().split(",")
    crabs_position = [int(item) for item in input]

    position_fuel_expensis = [0] * max(crabs_position)

    for index, pos in enumerate(position_fuel_expensis):
        for crab_pos in crabs_position:
            diff = abs(index - crab_pos)
            if diff != 0:
                position_fuel_expensis[index] += (1 + diff) * diff / 2

    print(min(position_fuel_expensis))
