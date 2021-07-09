# Breadth First Search

import Queue
import numpy as np

class Node:
    def __init__(self, value, parent, depth):
        self.value = value
        self.parent = parent
        self.depth = depth

def print_map(input_map):
    for i in range(input_map.shape[0]):
        temp = input_map[i].tostring()
        print(''.join(temp).decode('unicode-escape').encode('utf-8'))

def backtrack(map_used,goals):
    for points in goals:
        map_name = np.array([list(c) for c in map_used],dtype='|S6')
        back_track = points.parent
        while back_track:
            map_name[back_track.value[0],back_track.value[1]] = 'o'
            back_track = back_track.parent
        print('Path to goal {} at {}:'.format(goals.index(points)+1,tuple(points.value)))
        print_map(map_name)

def check_neighbor(input_map, parent_node, i, j):
    if parent_node == '\u2576':
        if input_map[i,j-1] in [' ','*']:
            if input_map[i+1,j] in [' ','*']:
                if input_map[i-1,j] in [' ','*']:
                    input_map[i,j] = '\u253c'
                else:
                    input_map[i,j] = '\u252c'
            elif input_map[i-1,j] in [' ','*']:
                input_map[i,j] = '\u2534'
            else :
                input_map[i,j] = '\u2500'
        elif input_map[i+1,j] in [' ','*']:
            if input_map[i-1,j] in [' ','*']:
                input_map[i,j] = '\u251c'
            else:
                input_map[i,j] = '\u250c'
        elif input_map[i-1,j] in [' ','*']:
            input_map[i,j] = '\u2514'
        else:
            input_map[i,j] = '\u2576'

    if parent_node == '\u2575':
        if input_map[i,j-1] in [' ','*']:
            if input_map[i+1,j] in [' ','*']:
                if input_map[i,j+1] in [' ','*']:
                    input_map[i,j] = '\u253c'
                else:
                    input_map[i,j] = '\u2524'
            elif input_map[i,j+1] in [' ','*']:
                input_map[i,j] = '\u2534'
            else :
                input_map[i,j] = '\u2518'
        elif input_map[i+1,j] in [' ','*']:
            if input_map[i,j+1] in [' ','*']:
                input_map[i,j] = '\u251c'
            else:
                input_map[i,j] = '\u2502'
        elif input_map[i,j+1] in [' ','*']:
            input_map[i,j] = '\u2514'
        else:
            input_map[i,j] = '\u2575'

    if parent_node == '\u2577':
        if input_map[i,j-1] in [' ','*']:
            if input_map[i,j+1] in [' ','*']:
                if input_map[i-1,j] in [' ','*']:
                    input_map[i,j] = '\u253c'
                else:
                    input_map[i,j] = '\u252c'
            elif input_map[i-1,j] in [' ','*']:
                input_map[i,j] = '\u2524'
            else :
                input_map[i,j] = '\u2510'
        elif input_map[i,j+1] in [' ','*']:
            if input_map[i-1,j] in [' ','*']:
                input_map[i,j] = '\u251c'
            else:
                input_map[i,j] = '\u250c'
        elif input_map[i-1,j] in [' ','*']:
            input_map[i,j] = '\u2502'
        else:
            input_map[i,j] = '\u2577'

    if parent_node == '\u2574':
        if input_map[i+1,j] in [' ','*']:
            if input_map[i,j+1] in [' ','*']:
                if input_map[i-1,j] in [' ','*']:
                    input_map[i,j] = '\u253c'
                else:
                    input_map[i,j] = '\u252c'
            elif input_map[i-1,j] in [' ','*']:
                input_map[i,j] = '\u2524'
            else :
                input_map[i,j] = '\u2510'
        elif input_map[i,j+1] in [' ','*']:
            if input_map[i-1,j] in [' ','*']:
                input_map[i,j] = '\u2534'
            else:
                input_map[i,j] = '\u2500'
        elif input_map[i-1,j] in [' ','*']:
            input_map[i,j] = '\u2518'
        else:
            input_map[i,j] = '\u2574'

def BFS(map_name,parent):

    frontier = Queue.Queue()
    frontier.put(parent)
    goal = []

    while not frontier.empty():
        current_node = frontier.get()

        if map_name[current_node.value[0],current_node.value[1]-1] in [' ','*']:
            if map_name[current_node.value[0],current_node.value[1]-1] == '*':
                goal.append(Node([current_node.value[0],current_node.value[1]-1], current_node, current_node.depth+1))
            frontier.put(Node([current_node.value[0],current_node.value[1]-1], current_node, current_node.depth+1))
            map_name[current_node.value[0],current_node.value[1]-1] = '\u2576'
            check_neighbor(map_name, map_name[current_node.value[0],current_node.value[1]-1], current_node.value[0],current_node.value[1]-1)

        if map_name[current_node.value[0]+1,current_node.value[1]] in [' ','*']:
            if map_name[current_node.value[0]+1,current_node.value[1]] == '*':
                goal.append(Node([current_node.value[0]+1,current_node.value[1]], current_node, current_node.depth+1))
            frontier.put(Node([current_node.value[0]+1,current_node.value[1]], current_node, current_node.depth+1))
            map_name[current_node.value[0]+1,current_node.value[1]] = '\u2575'
            check_neighbor(map_name, map_name[current_node.value[0]+1,current_node.value[1]], current_node.value[0]+1,current_node.value[1])

        if map_name[current_node.value[0],current_node.value[1]+1] in [' ','*']:
            if map_name[current_node.value[0],current_node.value[1]+1] == '*':
                goal.append(Node([current_node.value[0],current_node.value[1]+1], current_node, current_node.depth+1))
            frontier.put(Node([current_node.value[0],current_node.value[1]+1], current_node, current_node.depth+1))
            map_name[current_node.value[0],current_node.value[1]+1] = '\u2574'
            check_neighbor(map_name, map_name[current_node.value[0],current_node.value[1]+1], current_node.value[0],current_node.value[1]+1)

        if map_name[current_node.value[0]-1,current_node.value[1]] in [' ','*']:
            if map_name[current_node.value[0]-1,current_node.value[1]] == '*':
                goal.append(Node([current_node.value[0]-1,current_node.value[1]], current_node, current_node.depth+1))
            frontier.put(Node([current_node.value[0]-1,current_node.value[1]], current_node, current_node.depth+1))
            map_name[current_node.value[0]-1,current_node.value[1]] = '\u2577'
            check_neighbor(map_name, map_name[current_node.value[0]-1,current_node.value[1]], current_node.value[0]-1, current_node.value[1])

        print_map(map_name)
    return goal

# map1
maps = open('maps/map1.txt','r').read().splitlines()
map_name = np.array([list(c) for c in maps],dtype='|S6')
# finding s
row, col = np.where(map_name=='s')
parent = Node([row,col], None, 0)
# BFS
goals = BFS(map_name,parent)
backtrack(maps,goals)


# map2
maps = open('maps/map2.txt').read().splitlines()
map_name = np.array([list(c) for c in maps],dtype='|S6')
# finding s
row, col = np.where(map_name=='s')
parent = Node([row,col], None, 0)
# BFS
BFS(map_name,parent)

# map3
maps = open('maps/map3.txt').read().splitlines()
map_name = np.array([list(c) for c in maps],dtype='|S6')
# finding s
row, col = np.where(map_name=='s')
parent = Node([row,col], None, 0)
# BFS
BFS(map_name,parent)
