import copy, random
from prim_maze_generator import generate_maze, print_maze

height = int(input("Enter height of maze: "))
width = int(input("Enter width of maze: "))

global maze
maze = generate_maze(height, width, True)


def get_start_state(height, width):
#returns unchanging maze and opening("c") position on first row
    curr_position = None
    for i in range(height):
        for j in range(width):
            if maze[i][j] == 'c' and i == 0: #if i is first row
                    curr_position = (i, j)
                    break
        if curr_position:
            break
    start_state = maze, curr_position
    return start_state


def is_goal(state, height, width):
    # returns unchanging maze and closing("c") position on last row
    maze, curr_position = state
    goal_position = None
    for i in range(width):
        if maze[height-1][i] == 'c':
            goal_position = (height-1, i)
            break
    goal = maze, goal_position
    return state == goal



def next_states(state, height, width):
    maze, curr_position = state
    children = []

    # check if we can move up
    if curr_position[0] > 0 and maze[curr_position[0]-1][curr_position[1]] != 'w':
        new_position = (curr_position[0]-1, curr_position[1])
        new_state = maze, new_position
        children.append(new_state)

    # check if we can move down
    if curr_position[0] < height-1 and maze[curr_position[0]+1][curr_position[1]] != 'w':
        new_position = (curr_position[0]+1, curr_position[1])
        new_state = maze, new_position
        children.append(new_state)

    # check if we can move left
    if curr_position[1] > 0 and maze[curr_position[0]][curr_position[1]-1] != 'w':
        new_position = (curr_position[0], curr_position[1]-1)
        new_state = maze, new_position
        children.append(new_state)

    # check if we can move right
    if curr_position[1] < width-1 and maze[curr_position[0]][curr_position[1]+1] != 'w':
        new_position = (curr_position[0], curr_position[1]+1)
        new_state = maze, new_position
        children.append(new_state)

    return children


def print_state(maze):
    print_maze(maze)


