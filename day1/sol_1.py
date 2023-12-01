import aoc_lib

def sol_1(input):
    input_list = aoc_lib.file_to_array(input)
    answer_list=[]
    for line in input_list:
        numbers = []
        for i in range(len(line)):
            if line[i] >="0" and line[i] <= "9":
                numbers.append(int(line[i]))
        if len(numbers)==0:
            continue
        # print(numbers)
        output = numbers[-1] + numbers[0]*10
        answer_list.append(output)
    return sum(answer_list)

print(sol_1("data.txt"))