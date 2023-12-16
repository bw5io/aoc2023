import aoc_lib
import sys
sys.setrecursionlimit(10000000)
direction_dict = {
  'S': (0, 1),
  'N': (0, -1),
  'W': (-1, 0),
  'E': (1, 0)
}

def parse(input_list):
    current_matrix = []
    for i in input_list:
        if i=="":
            break
        else:
            current_matrix.append(list(i))
    return current_matrix

def ignite(matrix, final_matrix, pos_x=0, pos_y=0, direction='E'):
    if pos_y not in range(len(matrix)) or pos_x not in range(len(matrix[pos_y])) or direction in final_matrix[pos_y][pos_x]:
        return final_matrix
    next_directions = identify_next_direction(matrix[pos_y][pos_x], direction)
    final_matrix[pos_y][pos_x].append(direction)
    for next_direction in next_directions:
        step_x, step_y = direction_dict[next_direction]
        final_matrix = ignite(matrix, final_matrix, pos_x+step_x, pos_y+step_y, next_direction)
    return final_matrix

def identify_next_direction(symbol, direction):
    next_directions = []
    if symbol == '.':
        next_directions.append(direction)
    elif symbol =="\\":
        if direction == "N":
            next_directions.append("W")
        elif direction == "W":
            next_directions.append("N")
        elif direction == "S":
            next_directions.append("E")
        elif direction == "E":
            next_directions.append("S")
    elif symbol == "/":
        if direction == "N":
            next_directions.append("E")
        elif direction == "W":
            next_directions.append("S")
        elif direction == "S":
            next_directions.append("W")
        elif direction == "E":
            next_directions.append("N")
    elif symbol == "|":
        if direction in ['S', 'N']:
            next_directions.append(direction)
        elif direction in ['E', 'W']:
            next_directions.append('S')
            next_directions.append('N')
    elif symbol == "-":
        if direction in ['S', 'N']:
            next_directions.append('E')
            next_directions.append('W')
        elif direction in ['E', 'W']:
            next_directions.append(direction)
    return next_directions

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    matrix = parse(input_list)
    final_matrix = []
    for _ in range(len(matrix)):
        final_matrix_row = []
        for _ in range(len(matrix[0])):
            final_matrix_row.append([])
        final_matrix.append(final_matrix_row)
    print(final_matrix)
    final_matrix = ignite(matrix, final_matrix)
    count = 0
    for i in final_matrix:
        for j in i:
            if len(j)>0:
                print("#", end="")
                count+=1
            else:
                print(".", end="")
        print()
    return count

print(sol_1("data.txt"))