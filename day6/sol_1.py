import aoc_lib

def assess_record(time, record):
    possible_time = []
    for i in range(time):
        if i*(time-i)>record:
            possible_time.append(i)
    return len(possible_time)

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    time = [int(x) for x in input_list[0].split(" ")[1:] if x!='']
    record = [int(x) for x in input_list[1].split(" ")[1:] if x!='']
    answers = 1
    for i in range(len(time)):
        answers *= assess_record(time[i], record[i])
    return answers

print(sol_1("data1.txt"))