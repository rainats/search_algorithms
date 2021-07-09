# Iterative Depth First Search
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

def check_neighbor(input_map, path_map, current_arg):
    current_pos_index = path_map.index(current_arg.value)
    delta = np.array(current_arg.value) - np.array(current_arg.parent.value)
    i = path_map[current_pos_index][0]
    j = path_map[current_pos_index][1]

    if delta[1] == -1:
        if input_map[i,j-1] in [' ','*']:
            if input_map[i+1,j] in [' ','*']:
                if input_map[i-1,j] in [' ','*']:
                    result = '\u253c'
                else:
                    result = '\u252c'
            elif input_map[i-1,j] in [' ','*']:
                result = '\u2534'
            else :
                result = '\u2500'
        elif input_map[i+1,j] in [' ','*']:
            if input_map[i-1,j] in [' ','*']:
                result = '\u251c'
            else:
                result = '\u250c'
        elif input_map[i-1,j] in [' ','*']:
            result = '\u2514'
        else:
            result = '\u2576'

    if delta[0] == 1:
        if input_map[i,j-1] in [' ','*']:
            if input_map[i+1,j] in [' ','*']:
                if input_map[i,j+1] in [' ','*']:
                    result = '\u253c'
                else:
                    result = '\u2524'
            elif input_map[i,j+1] in [' ','*']:
                result = '\u2534'
            else :
                result = '\u2518'
        elif input_map[i+1,j] in [' ','*']:
            if input_map[i,j+1] in [' ','*']:
                result = '\u251c'
            else:
                result = '\u2502'
        elif input_map[i,j+1] in [' ','*']:
            result = '\u2514'
        else:
            result = '\u2575'

    if delta[0] == -1:
        if input_map[i,j-1] in [' ','*']:
            if input_map[i,j+1] in [' ','*']:
                if input_map[i-1,j] in [' ','*']:
                    result = '\u253c'
                else:
                    result = '\u252c'
            elif input_map[i-1,j] in [' ','*']:
                result = '\u2524'
            else :
                result = '\u2510'
        elif input_map[i,j+1] in [' ','*']:
            if input_map[i-1,j] in [' ','*']:
                result = '\u251c'
            else:
                result = '\u250c'
        elif input_map[i-1,j] in [' ','*']:
            result = '\u2502'
        else:
            result = '\u2577'

    if delta[1] == 1:
        if input_map[i+1,j] in [' ','*']:
            if input_map[i,j+1] in [' ','*']:
                if input_map[i-1,j] in [' ','*']:
                    result = '\u253c'
                else:
                    result = '\u252c'
            elif input_map[i-1,j] in [' ','*']:
                result = '\u2524'
            else :
                result = '\u2510'
        elif input_map[i,j+1] in [' ','*']:
            if input_map[i-1,j] in [' ','*']:
                result = '\u2534'
            else:
                result = '\u2500'
        elif input_map[i-1,j] in [' ','*']:
            result = '\u2518'
        else:
            result = '\u2574'
    return result

def IDFS(map_name,parent,limit):

    i = 0
    map_new = np.array(map_name)
    goal = []
    while i<limit:

        frontier_stack = []
        frontier_path = []
        frontier_stack.append(parent)
        frontier_path.append(parent)
        map_new = np.array(map_name)
        i = i+1

        while frontier_stack :

            current_node = frontier_stack.pop()
            if current_node.depth > 0:
                frontier_path.append(current_node.value)
                map_new[tuple(current_node.value)] = check_neighbor(map_new, frontier_path, current_node)
            # map_new[current_node.value[0],current_node.value[1]] = 'x'

            if current_node.depth < i:

                if map_new[current_node.value[0]-1,current_node.value[1]] == ' ' or map_new[current_node.value[0]-1,current_node.value[1]] == '*':
                    child4 = Node([current_node.value[0]-1,current_node.value[1]],current_node,current_node.depth+1)
                    if child4.value not in [n.value for n in frontier_stack]:
                        frontier_stack.append(child4)

                if map_new[current_node.value[0],current_node.value[1]+1] == ' ' or map_new[current_node.value[0],current_node.value[1]+1] == '*' :
                    child3 = Node([current_node.value[0],current_node.value[1]+1],current_node,current_node.depth+1)
                    if child3.value not in [n.value for n in frontier_stack]:
                        frontier_stack.append(child3)

                if map_new[current_node.value[0]+1,current_node.value[1]] == ' ' or map_new[current_node.value[0]+1,current_node.value[1]] == '*' :
                    child2 = Node([current_node.value[0]+1,current_node.value[1]],current_node,current_node.depth+1)
                    if child2.value not in [n.value for n in frontier_stack]:
                        frontier_stack.append(child2)

                if map_new[current_node.value[0],current_node.value[1]-1] == ' ' or map_new[current_node.value[0],current_node.value[1]-1] == '*' :
                    child1 = Node([current_node.value[0],current_node.value[1]-1],current_node,current_node.depth+1)
                    if child1.value not in [n.value for n in frontier_stack]:
                        frontier_stack.append(child1)

                if map_name[tuple(current_node.value)] == '*':
                    goal.append(current_node)

            print_map(map_new)
    return goal


# map1
maps = open('maps/map1.txt').read().splitlines()
map_name = np.array([list(c) for c in maps], dtype = '|S6')
row, col = np.where(map_name=='s')
parent = Node([row,col], None, 0)
goals = IDFS(map_name,parent,150)
backtrack(maps,goals)

# map2
# maps = open('maps/map2.txt').read().splitlines()
# map_name = np.array([list(c) for c in maps], dtype = '|S6')
# row, col = np.where(map_name=='s')
# parent = Node([row,col], None, 0)
# IDFS(map_name,parent,300)

#map3
# maps = open('maps/map3.txt').read().splitlines()
# map_name = np.array([list(c) for c in maps], dtype='|S6')
# row, col = np.where(map_name=='s')
# parent = Node([row,col], None, 0)
# IDFS(map_name,parent,500)
