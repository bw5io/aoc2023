import aoc_lib
# import re

def solve_1(sequence_list):
    if sequence_list.count(0)==len(sequence_list):
        return 0
    new_sequence_list=[]
    for i in range(len(sequence_list)-1):
        new_sequence_list.append(sequence_list[i+1]-sequence_list[i])
    return sequence_list[-1]+solve_1(new_sequence_list)

def parse_1(input_lines):
    lines = []
    for line in input_lines:
        if line == "":
            break
        lines.append([int(i) for i in line.split(" ")])
    return lines
        

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    sequence_lists = parse_1(input_list)
    return sum([solve_1(sequence_list) for sequence_list in sequence_lists])

print(sol_1("data1.txt"))
