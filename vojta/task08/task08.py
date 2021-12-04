import numpy as np


class BingoMatrix:
    def get_lookup_table(self, matrix):
        lookup_table = {}
        for x in range(len(matrix[0])):
            for y in range(len(matrix[:, 0])):
                lookup_table[matrix[x, y]] = (x, y)
        return lookup_table

    def fill_matrix_with_info(self, matrix):
        horizontal, vertical = np.ones(len(matrix[0])) * len(matrix[0]), np.ones(
            len(matrix[0]) + 1
        ) * len(matrix[0])
        matrix = np.append(matrix, [horizontal], axis=0)
        return np.append(matrix, vertical[:, None], axis=1)

    def __init__(self, matrix) -> None:
        self.lookup_table = self.get_lookup_table(matrix)
        self.matrix = self.fill_matrix_with_info(matrix)

    def do_final_computation(self, number):
        sum = 0
        for key in self.lookup_table:
            sum += key

        return sum * number

    def find_number(self, number):
        if number in self.lookup_table:
            x_coordinate, y_coordinate = self.lookup_table[number]
            self.matrix[x_coordinate, -1] -= 1
            self.matrix[-1, y_coordinate] -= 1

            del self.lookup_table[number]

            if self.matrix[x_coordinate, -1] == 0 or self.matrix[-1, y_coordinate] == 0:
                return self.do_final_computation(number)

            return None


def main():
    with open("input08.txt") as f:
        numbers = f.readline().split(",")
        boards = [int(x) for x in np.array(f.read().split())]
        boards = np.reshape(boards, (len(boards) // 25, 5, 5))
        bingo_boards = [BingoMatrix(board) for board in boards]
        for number in numbers:
            # creates copy of the list
            for bingo_board in bingo_boards[:]:
                value = bingo_board.find_number(int(number))
                if len(bingo_boards) == 1:
                    print(value)
                if value:
                    bingo_boards.remove(bingo_board)


if __name__ == "__main__":
    main()  # next section explains the use of sys.exit
