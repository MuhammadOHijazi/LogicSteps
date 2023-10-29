import state as stat
import actions as act
import solo_player as splay

if __name__ == '__main__':
    print("Logic steps Games")
    state = stat.State()
    print(state.grid)
    print(state.isfinal(state.grid))
    print("The postion of the start point is :", state.player)
    print("The postions of point grid[0][1] : ", state.grid[0][1])
    print("The postions of point grid[1][0] : ", state.grid[1][0])
    actions = act.Actions(state)
    print("Choose the way to solve the problem")
    meth = input("Enter 1 to play the game lonly\n "
                 "Enter 2 to solve the porblem using BFS algo\n "
                 "Enter 3 to solve the problem using DFS algo\n ")
    match meth:
        case "1":
            print("Start play the Game by your self")
            S_play = splay.Play(state, actions)
            S_play.plays(state.player)
        case "2":
            print("Solve the game by the Algorithms BFS")
        case "3":
            print("Solve the game by the  Algorithms DFS")
