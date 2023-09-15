"""Implementation of Breadth-First Search with pruning of visited
nodes. Relies on is_goal and next_states methods that must be imported from
elsewhere.

Sam Scott, Mohawk College, May 2022
ADAPTED BY JOHNDEE DAUFA, APRIL 09,2023
"""
## import Queue (Queue)
from queue import Queue

## import puzzle api
from maze_puzzle_definition import get_start_state, is_goal, height, width, next_states, print_state

closed = []                 # init open, closed
## solver
def BFS(start_state, height, width):

    open = Queue()
    open.put(start_state)

    while not open.empty():        # loop until no more open states

        state = open.get()         # get next state to expand

        if state not in closed:    # prune?

            closed.append(state)   # mark state visited (closed)

            if is_goal(state, height, width):     # success?
                return True

            for new_state in next_states(state, height, width):    # expand state
                open.put(new_state)                 # new states are open

    return False              # goal not found


## print the solution( maze and path(closed list marked with 'x'))
def print_solution():
    for state in closed:
        maze, curr_position = state
        maze[curr_position[0]][curr_position[1]] = '*'
    print_state(maze)

## run the solver

start_state = get_start_state(height, width)
result = BFS(start_state, height, width)
print(result)
print_solution()






