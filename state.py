import numpy as np


class State:
    player = (0, 0)

    def __init__(self):
        self.num_moves = 0
        self.row, self.columns, self.grid,self.player = self.grid_input()

    def grid_input(self):
        rows = int(input())
        columns = int(input())
        grid = np.array([[0] * columns] * rows)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                grid[i][j] = int(input())
        player_rows = int(input("Enter the Start point indexes for rows\n"))
        player_columns = int(input("Enter the Start point indexes for columns\n"))
        player = (player_rows, player_columns)
        return rows, columns, grid, player

    def isfinal(self, board):
        self.num_moves = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] != 0 and board[i][j] != -1:
                    self.num_moves += board[i][j]
        if self.num_moves > 0:
            print("There should be", self.num_moves, "moves To finish the game")
            return True
        else:
            return False
