import aoc_lib

def compare_difference(string_a, string_b):
    counter = 0
    for i in range(len(string_a)):
        if string_a[i]!=string_b[i]:
            counter+=1
    return counter

def find_column(matrix):
    for i in range(len(matrix[0])-1):
        check = compare_difference("".join([matrix[j][i] for j in range(len(matrix))]), "".join([matrix[j][i+1] for j in range(len(matrix))]))
        smudge_allowance = 1-check
        if smudge_allowance >= 0:
            counter = 1
            flag = False
            while i-counter>=0 and i+counter+1<len(matrix[0]):
                smudge_allowance -= compare_difference("".join([matrix[j][i-counter] for j in range(len(matrix))]), "".join([matrix[j][i+counter+1] for j in range(len(matrix))]))
                if smudge_allowance < 0:
                    flag = True
                    break
                counter+=1
            if flag==False and smudge_allowance==0:
                return i+1
    return 0

def find_row(matrix):
    for i in range(len(matrix)-1):
        check = compare_difference(matrix[i], matrix[i+1])
        smudge_allowance = 1-check
        if smudge_allowance >= 0:
            counter = 1
            flag = False
            while i-counter>=0 and i+counter+1<len(matrix):
                smudge_allowance -= compare_difference(matrix[i-counter], matrix[i+counter+1])
                if smudge_allowance < 0:
                    flag = True
                    break
                counter+=1
            if flag==False and smudge_allowance==0:
                return (i+1)*100
    return 0

def parse(input_list):
    all_matrices = []
    current_matrix = []
    for i in input_list:
        if i=="":
            all_matrices.append(current_matrix)
            current_matrix=[]
        else:
            current_matrix.append(i)
    return all_matrices

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    all_matrices = parse(input_list)
    outcome = 0
    for matrix in all_matrices:
        print(matrix)
        column_result = find_column(matrix)
        row_result = find_row(matrix)
        outcome+=column_result+row_result
        print(column_result, row_result)
    print(outcome)

print(sol_1("data.txt"))