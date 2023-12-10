import aoc_lib

def solve_2(sequence_list):
    if sequence_list.count(0)==len(sequence_list):
        return 0
    new_sequence_list=[]
    for i in range(len(sequence_list)-1):
        new_sequence_list.append(sequence_list[i+1]-sequence_list[i])
    return sequence_list[0]-solve_2(new_sequence_list)

def parse_2(input_lines):
    lines = []
    for line in input_lines:
        if line == "":
            break
        lines.append([int(i) for i in line.split(" ")])
    return lines
        

def sol_2(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    sequence_lists = parse_2(input_list)
    return sum([solve_2(sequence_list) for sequence_list in sequence_lists])

print(sol_2("data1.txt"))
