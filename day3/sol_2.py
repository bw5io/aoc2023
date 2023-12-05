import aoc_lib

def detect(matrix, x, y):
    check_list = [[(-1,0)],[(1,0)],[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)]]
    x_valid_range = range(len(matrix[y]))
    y_valid_range = range(len(matrix))
    valid_list = []
    for line in check_list:
        detect_flag = False
        for step_x, step_y in line:
            cur_x = x+step_x
            cur_y = y+step_y
            if detect_flag == True and matrix[cur_y][cur_x].isnumeric():
                break
            else:
                detect_flag = False
            temp_num = ""
            if cur_x in x_valid_range and cur_y in y_valid_range:
                if matrix[cur_y][cur_x].isnumeric():
                    detect_flag=True
                    temp_num=matrix[cur_y][cur_x]
                    cur_x_detect = cur_x-1
                    while cur_x_detect in x_valid_range:
                        if matrix[cur_y][cur_x_detect].isnumeric():
                            temp_num = matrix[cur_y][cur_x_detect]+temp_num
                            cur_x_detect-=1
                        else:
                            break
                    cur_x_detect = cur_x+1
                    while cur_x_detect in x_valid_range:
                        if matrix[cur_y][cur_x_detect].isnumeric():
                            temp_num = temp_num+matrix[cur_y][cur_x_detect]
                            cur_x_detect+=1
                        else:
                            break
                    valid_list.append(int(temp_num))
    if len(valid_list) == 2:
        print(valid_list)
        return valid_list[0]*valid_list[1]
    return 0

def sol_2(input):
    input_list = aoc_lib.file_to_array(input, return_matrix=True,allow_empty_line=False)
    num_valid = []

    for y in range(len(input_list)):
        if len(input_list[y])==0:
            break
        for x in range(len(input_list[y])):
            if input_list[y][x]=="*":
                num_valid.append(detect(input_list,x,y))
    return sum(num_valid)
    
print(sol_2("data1.txt"))