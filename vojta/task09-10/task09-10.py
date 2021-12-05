import numpy as np

with open("input09-10.txt") as f:
    input = f.read().split()
    coordinates = []
    for start, end in zip(input[::3], input[2::3]):
        start = [int(x) for x in start.split(",")]
        end = [int(x) for x in end.split(",")]
        coordinates.append([start, end])

    max_coordinate = max([max(y) for y in [max(x) for x in coordinates]])
    array = np.zeros((max_coordinate + 1, max_coordinate + 1))

    for coordinate in coordinates:
        start_x, start_y, end_x, end_y = (
            coordinate[0][0],
            coordinate[0][1],
            coordinate[1][0],
            coordinate[1][1],
        )
        # horizontal line
        if start_y == end_y:
            if start_x > end_x:
                start_x, end_x = end_x, start_x
            diff = abs(start_x - end_x)
            for i in range(diff + 1):
                array[start_y, start_x + i] += 1
        # vertical
        elif start_x == end_x:
            if start_y > end_y:
                start_y, end_y = end_y, start_y
            diff = abs(start_y - end_y)
            for i in range(diff + 1):
                array[start_y + i, start_x] += 1
        # diogonal
        else:
            if start_y > end_y:
                start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
            diff = abs(start_x - end_x)
            # left to right
            if start_x < end_x:
                for i in range(diff + 1):
                    array[start_y + i, start_x + i] += 1
            else:
                for i in range(diff + 1):
                    array[start_y + i, start_x - i] += 1

    occurences, count = np.unique(array.flatten(), return_counts=True)
    print(sum(count[2:]))
