import aoc_lib
from functools import cache

def parse(input_list):
    current_matrix = []
    for i in input_list:
        if i=="":
            break
        else:
            current_matrix.append(tuple(i))
    return tuple(current_matrix)

@cache
def one_round(matrix):
    matrix = roll_north(matrix)
    matrix = roll_west(matrix)
    matrix = roll_south(matrix)
    matrix = roll_east(matrix)
    return matrix

@cache
def roll_north(matrix):
    counter = 0
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for _ in range(len(matrix[i])):
            new_matrix[i].append(".")
    for i in range(len(matrix[0])):
        current_line = 0
        for j in range(len(matrix)):
            if matrix[j][i]=="O":
                new_matrix[current_line][i]="O"
                current_line+=1
            elif matrix[j][i]=="#":
                current_line=j+1
                new_matrix[j][i]="#"
    return tuple([tuple(i) for i in new_matrix])

@cache
def roll_east(matrix):
    counter = 0
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for _ in range(len(matrix[i])):
            new_matrix[i].append(".")
    for i in range(len(matrix)):
        current_row = len(matrix[i])-1
        for j in range(len(matrix[i])-1,-1,-1):
            if matrix[i][j]=="O":
                new_matrix[i][current_row]="O"
                current_row-=1
            elif matrix[i][j]=="#":
                current_row=j-1
                new_matrix[i][j]="#"
    return tuple([tuple(i) for i in new_matrix])

@cache
def roll_south(matrix):
    counter = 0
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for _ in range(len(matrix[i])):
            new_matrix[i].append(".")
    for i in range(len(matrix[0])):
        current_line = len(matrix)-1
        for j in range(len(matrix)-1,-1,-1):
            if matrix[j][i]=="O":
                new_matrix[current_line][i]="O"
                current_line-=1
            elif matrix[j][i]=="#":
                current_line=j-1
                new_matrix[j][i]="#"
    return tuple([tuple(i) for i in new_matrix])

@cache
def roll_west(matrix):
    counter = 0
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for _ in range(len(matrix[i])):
            new_matrix[i].append(".")
    for i in range(len(matrix)):
        current_row = 0
        for j in range(len(matrix[i])):
            if matrix[i][j]=="O":
                new_matrix[i][current_row]="O"
                current_row+=1
            elif matrix[i][j]=="#":
                current_row=j+1
                new_matrix[i][j]="#"
    return tuple([tuple(i) for i in new_matrix])

def calculate_tilted_board(matrix):
    counter = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i]=="O":
                counter+=len(matrix)-j
    return counter

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    matrix = parse(input_list)
    for i in matrix:
        print("".join(i))
    outcome=[]
    to_be_checked=[]
    to_be_validated=[]
    pattern=[]
    i=0
    while True: 
        matrix=one_round(matrix)
        current_outcome=calculate_tilted_board(matrix)
        new_to_be_validated = []
        new_to_be_checked = []
        break_flag = False
        for this_round in to_be_validated:
            if i==this_round["Tail"]+2*(this_round["Tail"]-this_round["Head"]+1):
                pattern=this_round
                break_flag=True
                break
            if current_outcome==outcome[i-2*(this_round["Tail"]-this_round["Head"]+1)]:
                new_to_be_validated.append(this_round)
        if break_flag == True:
            break
        to_be_validated = new_to_be_validated
        for this_round in to_be_checked:
            if i==this_round["Tail"]+(this_round["Tail"]-this_round["Head"]+1):
                to_be_validated.append(this_round)
            elif current_outcome==outcome[i-(this_round["Tail"]-this_round["Head"]+1)]:
                new_to_be_checked.append(this_round)
        to_be_checked = new_to_be_checked
        if current_outcome in outcome:
            to_be_checked.append({"Head": len(outcome) - 1 -outcome[::-1].index(current_outcome), "Tail":i-1})
        outcome.append(current_outcome)
        i+=1
    print(outcome, pattern, i)
    length = pattern["Tail"]-pattern["Head"]+1
    index_to_be = (1000000000-pattern["Tail"]-1) % length + pattern["Tail"]
    return outcome[index_to_be]
print(sol_1("test.txt"))
print(sol_1("data.txt"))