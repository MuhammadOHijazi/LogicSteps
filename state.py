import numpy as np
import collections


class State:
    player = (0, 0)

    def __init__(self):
        self.get_next_state_stack = []
        self.num_moves = 0
        self.row, self.columns, self.grid, self.player = self.grid_input()
        self.next_state = self.grid

    def grid_input(self):
        rows = int(input("Enter the number of rows\n"))
        columns = int(input("Enter the number of columns\n"))
        grid = np.array([[0] * columns] * rows)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                grid[i][j] = int(input())
        player_rows = int(input("Enter the Start point indexes for rows\n"))
        player_columns = int(input("Enter the Start point indexes for columns\n"))
        self.player = (player_rows, player_columns)
        return rows, columns, grid, self.player

    # next state will get the  place of cell
    def get_next_state(self, neighbors_list, board):
        for i in range(0, len(neighbors_list)):
            self.next_state = board
            cell_to_move = neighbors_list[i]
            player_row, player_column = cell_to_move
            self.next_state = np.copy(board)
            self.next_state[player_row][player_column] -= 1
            self.get_next_state_stack.append(self.next_state)

        # for testing
        for i in range(0, len(self.get_next_state_stack)):
            print("This is the", i, "state in the get next stae\n", self.get_next_state_stack[i])

    def isfinal(self, board):
        self.num_moves = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] != 0 and board[i][j] != -1:
                    self.num_moves += board[i][j]
        if self.num_moves > 0:
            print("There should be", self.num_moves, "moves To finish the game")
            return False
        else:
            return True
