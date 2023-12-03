import aoc_lib

def sol_1(input):
    input_list = aoc_lib.file_to_array(input, return_matrix=True)
    num_temp = ""
    num_valid = []
    symbol_flag = False
    
    for y in range(len(input_list)):
        if len(input_list[y])==0:
            break
        print(input_list[y])

print(sol_1("test1.txt"))