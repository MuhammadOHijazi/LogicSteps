class Play:

    def __init__(self, state, actions):
        self.new_place = (0, 0)
        self.actions = actions
        self.state = state
        self.move = ''
        self.player = self.state.player

    def plays(self, player):
        player_row, player_column = player
        while self.move != 'Q':
            print("The current state is:\n", self.actions.new_state)
            self.move = input("Enter the place you want to go:\n "
                              "L for left\n"
                              "R for Right\n"
                              "W for front\n"
                              "S for back\n"
                              "Q for stop the game\n")
            match self.move:
                case "l":
                    player_column -= 1
                    new_p = (player_row, player_column)
                    print("The destination target in this move is :", new_p)
                    state = self.actions.valid_action(self.actions.new_state, self.player, new_p)
                    print("The state is :", state)
                    if state:
                        self.new_place = new_p
                        self.player = self.actions.player_move(self.new_place, self.actions.new_state)
                        print("The player should be in the postion:", self.player)
                    else:
                        new_p = player
                        player_column += 1
                        print("we have been returned to the postion :", new_p)
                case "r":
                    player_column += 1
                    new_p = (player_row, player_column)
                    print("The destination target in this move is :", new_p)
                    state = self.actions.valid_action(self.actions.new_state, self.player, new_p)
                    print("The state is :", state)
                    if state:
                        self.new_place = new_p
                        self.player = self.actions.player_move(self.new_place, self.actions.new_state)
                        print("The player should be in the postion:", self.player)
                    else:
                        new_p = player
                        player_column -= 1
                        print("we have been returned to the postion :", new_p)
                case "w":
                    player_row -= 1
                    new_p = (player_row, player_column)
                    print("The destination target in this move is :", new_p)
                    state = self.actions.valid_action(self.actions.new_state, self.player, new_p)
                    print("The state is :", state)
                    if state:
                        self.new_place = new_p
                        self.player = self.actions.player_move(self.new_place, self.actions.new_state)
                        print("The player should be in the postion:", self.player)
                    else:
                        new_p = player
                        player_row += 1
                        print("we have been returned to the postion :", new_p)
                case "s":
                    player_row += 1
                    new_p = (player_row, player_column)
                    print("The destination target in this move is :", new_p)
                    state = self.actions.valid_action(self.actions.new_state, self.player, new_p)
                    print("The state is :", state)
                    if state:
                        self.new_place = new_p
                        self.player = self.actions.player_move(self.new_place, self.actions.new_state)
                        print("The player should be in the postion:", self.player)
                    else:
                        new_p = player
                        player_row -= 1
                        print("we have been returned to the postion :", new_p)
                case "q":
                    print("The game has been stopped")
                    return
            if self.state.isfinal(self.actions.new_state):
                print("You have finish the game\n")
                print("The states you have been moved on to pass is:\n")
                for i in range(0,len(self.actions.stack)):
                    print("\nThe", i, "State\n",self.actions.stack[i])

                return

