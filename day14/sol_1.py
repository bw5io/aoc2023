import aoc_lib

def parse(input_list):
    current_matrix = []
    for i in input_list:
        if i=="":
            break
        else:
            current_matrix.append(list(i))
    return current_matrix

def calculate_tilted_board(matrix):
    counter = 0
    for i in range(len(matrix[0])):
        current_weight = len(matrix)
        for j in range(len(matrix)):
            if matrix[j][i]=="O":
                counter+=current_weight
                current_weight-=1
            elif matrix[j][i]=="#":
                current_weight=len(matrix)-j-1
                print(j, i)
    return counter

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    matrix = parse(input_list)
    return calculate_tilted_board(matrix)

print(sol_1("data.txt"))