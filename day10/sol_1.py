import aoc_lib

tiles = {
    "F": {"S", "E"},
    "-": {"E", "W"},
    "7": {"S", "W"},
    "J": {"N", "W"},
    "L": {"N", "E"},
    "|": {"N", "S"}
}

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

def find_furthest(matrix, starting_point):
    next_steps = []
    distance_map = {get_dict_key(starting_point['position'][0], starting_point['position'][1]): 0}
    distance=1
    next_steps.append(get_next_steps(starting_point['position'][0], starting_point['position'][1], starting_point['direction']))
    while next_steps:
        this_steps = next_steps.pop(0)
        new_next_steps=[]
        for i in this_steps:
            if get_dict_key(i[0],i[1]) in distance_map.keys():
                continue
            distance_map[get_dict_key(i[0],i[1])]=distance
            new_next_steps+=get_next_steps(i[0],i[1],matrix[i[1]][i[0]])
        if new_next_steps: next_steps.append(new_next_steps)
        distance+=1
    return max(distance_map.values())

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    matrix = parse(input_list)
    starting_point = find_start(matrix)
    distance=find_furthest(matrix, starting_point)
    return distance

print(sol_1("data.txt"))
