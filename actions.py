import numpy as np
import collections as collect


class Actions:
    stack = collect.deque()

    def __init__(self, state):
        self.new_stack = []
        self.next_state = state.grid
        self.new_state = state.grid
        self.player = state.player
        self.neighbors_list = []
        self.state = state
        self.player_column = 0
        self.player_row = 0

    # get all the neighbors from the cell that send that the player get move to it
    def get_neighbors(self, player_place, board):
        i, j = player_place
        neighboring_cells = []
        for y in range(max(i - 1, 0), min(i + 2, len(board))):
            for x in range(max(j - 1, 0), min(j + 2, len(board[0]))):
                # check the nereby cells
                if (i, j) != (y, x) and ((abs(y - i)) != 1 or (abs(x - j) != 1)):
                    # check if the cell is valid to move
                    if board[y][x] >= 1:
                        neighboring_cells.append((y, x))

        self.neighbors_list = np.array(neighboring_cells)
        # print all the neighbors
        print("The neighbors for the player place is:\n")
        for i in range(0, len(self.neighbors_list)):
            print(self.neighbors_list[i])

    def valid_action(self, board, cell, player_place):
        # call get_neighbors functions to get all the valid places
        self.get_neighbors(player_place, board)
        # for testing call
        # do the get_next_state function here
        print("This is an optional moves that could you move")
        self.state.get_next_state(self.neighbors_list, board)

        # check that the move request is valid
        if cell in self.neighbors_list:
            return True
        else:
            return False

    # player move is the function that create the new state when we move to a valid cell
    def player_move(self, cell, board):
        player_row, player_column = cell
        player = (player_row, player_column)
        # change the value of the grid because of the move
        self.stack.append(board)
        self.new_state = np.copy(board)
        self.new_state[player_row][player_column] -= 1
        print("The new board is\n", self.new_state)
        return player


