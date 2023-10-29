import state as stat
import actions as act
if __name__ == '__main__':
    print("Logic steps Games")
    state = stat.State()
    print(state.grid)
    print(state.isfinal(state.grid))
    print("The postion of the start point is :", state.player)
    print("The postions of point grid[0][1] : ", state.grid[0][1])
    print("The postions of point grid[1][0] : ", state.grid[1][0])
    actions = act.Actions()
    actions.valid_action(state.grid, state.player)


