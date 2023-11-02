class Play:

    def __init__(self, state, actions):
        self.new_place = (0, 0)
        self.actions = actions
        self.state = state
        self.move = ''

    def plays(self):
        while True:
            player_row, player_column = self.state.player
            print("The current state is:\n", self.actions.new_state)
            print("The player place should be in:\n", self.state.player)
            self.move = input("\nEnter the place you want to go:\n "
                              "A for left\n"
                              "D for Right\n"
                              "W for front\n"
                              "S for back\n"
                              "Q for stop the game\n")

            match self.move:
                case "d":
                    player_column += 1
                    new_possible_positions = (player_row, player_column)
                    print("You want the player to move to:", new_possible_positions)
                    check_valid = self.actions.valid_action(self.actions.new_state, new_possible_positions,
                                                            self.state.player)
                    if check_valid:
                        self.state.player = self.actions.player_move(new_possible_positions, self.actions.new_state)
                        self.state.get_next_state_stack = []
                    else:
                        player_column -= 1
                        new_possible_positions = (player_row, player_column)
                        print("This move is non valid")
                        self.state.player = new_possible_positions
                        print("the player should return to the place",self.state.player)
                case "a":
                    player_column -= 1
                    new_possible_positions = (player_row, player_column)
                    print("You want the player to move to:", new_possible_positions)
                    check_valid = self.actions.valid_action(self.actions.new_state, new_possible_positions,
                                                            self.state.player)
                    if check_valid:
                        self.state.player = self.actions.player_move(new_possible_positions, self.actions.new_state)
                        self.state.get_next_state_stack = []
                    else:
                        player_column += 1
                        new_possible_positions = (player_row, player_column)
                        print("This move is non valid")
                        self.state.player = new_possible_positions
                        print("the player should return to the place",self.state.player)
                case "w":
                    player_row -= 1
                    new_possible_positions = (player_row, player_column)
                    print("You want the player to move to:", new_possible_positions)
                    check_valid = self.actions.valid_action(self.actions.new_state, new_possible_positions,
                                                            self.state.player)
                    if check_valid:
                        self.state.player = self.actions.player_move(new_possible_positions, self.actions.new_state)
                        self.state.get_next_state_stack = []
                    else:
                        player_column += 1
                        new_possible_positions = (player_row, player_column)
                        print("This move is non valid")
                        self.state.player = new_possible_positions
                        print("the player should return to the place", self.state.player)
                case "s":
                    player_row += 1
                    new_possible_positions = (player_row, player_column)
                    print("You want the player to move to:", new_possible_positions)
                    check_valid = self.actions.valid_action(self.actions.new_state, new_possible_positions,
                                                            self.state.player)
                    if check_valid:
                        self.state.player = self.actions.player_move(new_possible_positions, self.actions.new_state)
                        self.state.get_next_state_stack = []
                    else:
                        player_row -= 1
                        new_possible_positions = (player_row, player_column)
                        print("This move is non valid")
                        self.state.player = new_possible_positions
                        print("the player should return to the place", self.state.player)

                case _:
                    print("The game has been stopped")
                    return
            final_check = self.state.isfinal(self.actions.new_state)
            if final_check:
                print("The game has been finsih")
                return
            else:
                if len(self.actions.neighbors_list) == 0:
                    print("You have been Lost the game")
                    return
                else:
                    continue
