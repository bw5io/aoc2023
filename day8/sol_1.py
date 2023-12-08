import aoc_lib
import re

def parse(input_list):
    instructions=list(input_list.pop(0))
    input_list.pop(0)

    map_data = {}
    for i in input_list:
        if len(i)==0:
            break
        splitted_line = i.split("=")
        map_key = splitted_line[0].strip()
        map_value = [str(re.sub('[^A-Za-z]+', '', i)) for i in splitted_line[1].split(",")]
        map_data[map_key]={"L": map_value[0], "R": map_value[1]}
    return instructions, map_data

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    instructions, data = parse(input_list)
    print(instructions, data)
    location = "AAA"
    move_count = 0
    i=0
    while location != "ZZZ":
        if i>=len(instructions):
            i=0
        location = data[location][instructions[i]]
        move_count+=1
        i+=1
    return move_count

print(sol_1("data1.txt"))