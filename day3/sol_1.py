import aoc_lib

def detect(matrix, x, y):
    check_list = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    x_valid_range = range(len(matrix[y]))
    y_valid_range = range(len(matrix))
    for step_x, step_y in check_list:
        if x+step_x in x_valid_range and y+step_y in y_valid_range:
            if matrix[y+step_y][x+step_x]!="." and matrix[y+step_y][x+step_x].isnumeric() == False:
                return True
    return False

def sol_1(input):
    input_list = aoc_lib.file_to_array(input, return_matrix=True,allow_empty_line=False)
    num_temp = ""
    num_valid = []
    symbol_flag = False

    for y in range(len(input_list)):
        if len(input_list[y])==0:
            break
        for x in range(len(input_list[y])):
            if input_list[y][x].isnumeric():
                num_temp+=input_list[y][x]
                symbol_flag = symbol_flag or detect(input_list,x,y)
            else:
                if num_temp!="":
                    if symbol_flag == True: num_valid.append(int(num_temp))
                    num_temp=""
                    symbol_flag=False
        if num_temp!="":
            if symbol_flag == True: num_valid.append(int(num_temp))
            num_temp=""
            symbol_flag=False
    return sum(num_valid)
    
print(sol_1("data1.txt"))