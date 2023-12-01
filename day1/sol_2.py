import aoc_lib

def sol_2(input):
    input_list = aoc_lib.file_to_array(input)
    answer_list=[]
    for line in input_list:
        numbers = []
        for i in range(len(line)):
            if line[i] >="0" and line[i] <= "9":
                numbers.append(int(line[i]))
            else:
                try:
                    if line[i:i+3] == "one":
                        numbers.append(1)
                    elif line[i:i+3] == "two":
                        numbers.append(2)
                    elif line[i:i+3] == "six":
                        numbers.append(6)
                    elif line[i:i+4] == "four":
                        numbers.append(4)
                    elif line[i:i+4] == "five":
                        numbers.append(5)
                    elif line[i:i+4] == "nine":
                        numbers.append(9)
                    elif line[i:i+4] == "zero":
                        numbers.append(0)
                    elif line[i:i+5] == "seven":
                        numbers.append(7)
                    elif line[i:i+5] == "eight":
                        numbers.append(8)
                    elif line[i:i+5] == "three":
                        numbers.append(3)
                except:
                    pass
        if len(numbers)==0:
            continue
        print(numbers)
        output = numbers[-1] + numbers[0]*10
        answer_list.append(output)
    return sum(answer_list)

print(sol_2("data.txt"))