import aoc_lib

def find_column(matrix):
    for i in range(len(matrix[0])-1):
        if "".join([matrix[j][i] for j in range(len(matrix))]) == "".join([matrix[j][i+1] for j in range(len(matrix))]):
            counter = 1
            flag = False
            while i-counter>=0 and i+counter+1<len(matrix[0]):
                if "".join([matrix[j][i-counter] for j in range(len(matrix))]) != "".join([matrix[j][i+counter+1] for j in range(len(matrix))]):
                    flag = True
                    break
                counter+=1
            if flag==False:
                return i+1
    return 0

def find_row(matrix):
    for i in range(len(matrix)-1):
        if matrix[i]==matrix[i+1]:
            counter = 1
            flag = False
            while i-counter>=0 and i+counter+1<len(matrix):
                if matrix[i-counter]!=matrix[i+counter+1]:
                    flag = True
                    break
                counter+=1
            if flag==False:
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