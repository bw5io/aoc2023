import aoc_lib

def get_question_mark(spring_map):
    question_mark_locations = []
    for i in range(len(spring_map)):
        if spring_map[i]=="?":
            question_mark_locations.append(i)
    return question_mark_locations

def validate(spring_map, pattern):
    in_spring_flag = False
    springs = []
    spring_width = 0
    for i in spring_map:
        if i==".":
            if in_spring_flag==True:
                springs.append(spring_width)
                spring_width = 0
            in_spring_flag=False
        if i=="#":
            in_spring_flag = True
            spring_width+=1
    if in_spring_flag==True:
        springs.append(spring_width)
    # print(pattern, springs)
    if len(pattern)!=len(springs):
        return 0
    for i in range(len(pattern)):
        if pattern[i]!=springs[i]:
            return 0
    return 1

def brute_force(spring_map, question_mark_locations, pattern):
    if len(question_mark_locations)==0:
        count = validate(spring_map, pattern)
        # print(spring_map, count)
        return count
    possibility=["#", "."]
    current_question_mark = question_mark_locations[0]
    possible_solutions = 0
    for i in possibility:
        current_spring_map = [i for i in spring_map]
        current_spring_map[current_question_mark]=i
        possible_solutions+=brute_force(current_spring_map, question_mark_locations[1:], pattern)
    return possible_solutions

def parse(text_list):
    springs = []
    for i in text_list:
        if len(i)==0:
            continue
        spring = i.split(" ")[0]
        pattern_text = i.split(" ")[1]
        pattern = [int(j) for j in pattern_text.split(",")]
        springs.append({"Spring": spring, "Pattern": pattern})
    return springs

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    springs = parse(input_list)
    valid_possibilities = 0
    for i in springs:
        question_mark_locations=get_question_mark(i["Spring"])
        current_possibility = brute_force(i["Spring"], question_mark_locations, i["Pattern"])
        print(i, current_possibility)
        valid_possibilities+=current_possibility
    return valid_possibilities

print(sol_1("data.txt"))