import numpy as np
import collections as collect


class Actions:
    stack = collect.deque()

    def __init__(self, state):
        self.new_state = state.grid
        self.neighbors_list = []
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

    def valid_action(self, board, player, cell):
        print("Here is the valid action function")
        self.player_row, self.player_column = player
        # get all the neighbors of the cell that player stopped in
        neighbors_list = self.neighbors(player, board)
        self.neighbors_list = np.array(neighbors_list)
        # print all the neighbors
        for i in range(0, len(neighbors_list)):
            print(neighbors_list[i])
        # check that the move request is valid
        if cell in neighbors_list:
            return True
        else:
            return False

    # player move is the function that create the new state when we move to a valid cell
    def player_move(self, cell, board):
        if cell in self.neighbors_list:
            player_row, player_column = cell
            player = (player_row, player_column)
            # change the value of the grid because of the move
            self.stack.append(board)
            self.new_state = np.copy(board)
            self.new_state[player_row][player_column] -= 1
            print("The new board is\n", self.new_state)
            return player


