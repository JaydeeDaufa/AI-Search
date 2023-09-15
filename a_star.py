"""Implementation of A* Search with pruning of visited
nodes. Relies on is_goal and next_states methods that must be imported from
elsewhere.

Sam Scott, Mohawk College, May 2022
ADAPTED BY JOHNDEE DAUFA, APRIL 09,2023
"""

"""
Manhattan distance is the sum of the absolute differences between the horizontal and vertical coordinates. I used it in the maze problem because it is the minimum number of steps required to move from the current position to the next position if only horizontal and vertical moves are allowed. It is also consistent allowing one move at a time and doesn't overextend maze

"""
## import PriorityQueue (priority queue)
from queue import PriorityQueue
import math

## import puzzle api
from maze_puzzle_definition import get_start_state, is_goal, height, width, next_states, print_state

closed = []

def manhattan_distance(curr_position, next_position): #heuristic function
    return abs(curr_position[0] - next_position[0]) + abs(curr_position[1] - next_position[1])


## solver
def BEFS(start_state, height, width):
    open = PriorityQueue()
    open.put((0, start_state))  # add tuple with fvalue as first element

    while not open.empty():
        fvalue, state = open.get()  # get state with smallest fvalue

        if state not in closed:
            closed.append(state)

            if is_goal(state, height, width):
                return True

            for new_state in next_states(state, height, width):
                new_fvalue = fvalue + manhattan_distance(state[1], new_state[1])  # calculate new fvalue
                open.put((new_fvalue, new_state))  # add tuple with new fvalue

    return False


def print_solution():
    for state in closed:
        maze, curr_position = state
        maze[curr_position[0]][curr_position[1]] = '*'
    print_state(maze)



start_state = get_start_state(height, width)
result= BEFS(start_state, height, width)
print(result)
print_solution()








