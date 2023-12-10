import aoc_lib
import sys
import time

tiles = {
    "F": {"S", "E"},
    "-": {"E", "W"},
    "7": {"S", "W"},
    "J": {"N", "W"},
    "L": {"N", "E"},
    "|": {"N", "S"}
}
corner_tiles = ["F", "7", "J", "L"]
directions = {
    "S": [1,0],
    "N": [-1,0],
    "W": [0,-1],
    "E": [0,1],
}

def parse(input_list):
    lines = []
    for line in input_list:
        if line!="":
            lines.append(list(line))
    return lines

def get_dict_key(x,y):
    return f"x{x}y{y}"

def find_start(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x]=="S":
                connected = set()
                for direction, step in directions.items():
                    step_y = y-step[0]
                    step_x = x-step[1]
                    if step_y in range(len(matrix)) and step_x in range(len(matrix[0])):
                        if matrix[step_y][step_x] in tiles.keys():
                            if direction in tiles[matrix[step_y][step_x]]:
                                connected.add(direction)
                if connected in [tiles["-"], tiles["|"]]:
                    tile = list(tiles.keys())[list(tiles.values()).index(connected)]
                else:
                    tile = list(tiles.keys())[list(tiles.values()).index({"N", "W", "E", "S"}-connected)]
                return {"position": [x,y], "direction": tile}
            
def get_next_steps(x,y,this_direction):
    next_steps = []
    for direction in tiles[this_direction]:
        new_y = y+directions[direction][0]
        new_x = x+directions[direction][1]
        next_steps.append([new_x, new_y])
    return next_steps

def find_boundaries(matrix, starting_point):
    next_steps = []
    boundaries = [[starting_point['position'][0], starting_point['position'][1]]]
    next_steps.append(get_next_steps(starting_point['position'][0], starting_point['position'][1], starting_point['direction']))
    while next_steps:
        this_steps = next_steps.pop(0)
        new_next_steps=[]
        for i in this_steps:
            if i in boundaries:
                continue
            boundaries.append(i)
            new_next_steps+=get_next_steps(i[0],i[1],matrix[i[1]][i[0]])
        if new_next_steps: next_steps.append(new_next_steps)
    return boundaries

def detect(matrix, boundaries):
    inside_path_area=False
    previous_corner=""
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if [x,y] not in boundaries:
                if previous_corner!="":
                    previous_corner=""
                    inside_path_area = not inside_path_area
                if inside_path_area == True:
                    matrix[y][x]="."
                else:
                    matrix[y][x]=" "
            else:
                if matrix[y][x]=="|":
                    inside_path_area = not inside_path_area
                elif matrix[y][x]=="-":
                    continue
                else:
                    if previous_corner=="":
                        previous_corner=matrix[y][x]
                    else:
                        if len(tiles[previous_corner].union(tiles[matrix[y][x]]))==4:
                            inside_path_area = not inside_path_area
                            previous_corner=""
                        else:
                            previous_corner=""
    return matrix

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    matrix = parse(input_list)
    starting_point = find_start(matrix)
    boundaries=find_boundaries(matrix, starting_point)
    matrix[starting_point['position'][1]][starting_point['position'][0]]=starting_point["direction"]
    # c=detect(matrix, boundaries)
    # for y in c:
    #     for x in y:
    #         print(x, end='')
    #     print("")
    count_dot=0
    for y in matrix:
        count_dot+=y.count(".")
    return(count_dot)

start=time.time()
print(sol_1("data.txt"))
end=time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")