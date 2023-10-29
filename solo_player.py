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
                case "q":
                    print(self.actions.stack)
                    return
            if self.state.isfinal(self.actions.new_state):
                print("You have finish the game\n")
                return

