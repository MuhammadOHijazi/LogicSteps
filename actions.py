import numpy as np


class Actions:
    def __init__(self):
        self.player_column = 0
        self.player_row = 0

    @staticmethod
    def neighbors(cell, board):
        i, j = cell
        neighboring_cells = []
        for y in range(max(i - 1, 0), min(i + 2, len(board))):
            for x in range(max(j - 1, 0), min(j + 2, len(board[0]))):
                # check the nereby cells
                if (i, j) != (y, x) and ((abs(y - i)) != 1 or (abs(x - j) != 1)):
                    # check if the cell is valid to move
                    if board[y][x] >= 1:
                        neighboring_cells.append((y, x))
        return neighboring_cells

    def valid_action(self, board, player):
        print("Here is the valid action function")
        self.player_row, self.player_column = player
        neighbors_list = self.neighbors(player, board)
        neighbors_list = np.array(neighbors_list)
        for i in range(0, len(neighbors_list)):
            print(neighbors_list[i])
