import aoc_lib

def assess_record(time, record):
    for i in range(time):
        if i*(time-i)>record:
            print(i)
            return time-i*2+1

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    time = int("".join([x for x in input_list[0].split(" ")[1:] if x!='']))
    record = int("".join([x for x in input_list[1].split(" ")[1:] if x!='']))
    answers = assess_record(time, record)
    return answers

# print(sol_1("test1.txt"))
# print(sol_1("data1.txt"))