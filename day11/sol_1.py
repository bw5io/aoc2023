import aoc_lib

class galaxy():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"<Galaxy x: {self.x} y: {self.y}>"

def parse(input_list):
    lines = []
    for line in input_list:
        if line!="":
            lines.append(list(line))
    return lines

def get_stars(matrix):
    stars=[]
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x]=="#":
                stars.append(galaxy(x,y))
    return stars

def get_lines_width(matrix):
    column=[]
    row = []
    for i in matrix:
        if i.count("#")==0:
            row.append(2)
        else:
            row.append(1)
    for i in range(len(matrix[0])):
        if [matrix[y][i] for y in range(len(matrix))].count("#")==0:
            column.append(2)
        else:
            column.append(1)
    return row, column

def get_stars_distance(star1, star2, row_length, column_length):
    column_distance = sum(column_length[min([star1.x, star2.x]):max([star1.x, star2.x])])
    row_distance = sum(row_length[min([star1.y, star2.y]):max([star1.y, star2.y])])
    return column_distance+row_distance

def calculate(stars, row_length, column_length):
    distances=[]
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            distances.append(get_stars_distance(stars[i], stars[j], row_length, column_length))
    return sum(distances)

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    matrix = parse(input_list)
    stars = get_stars(matrix)
    row_length, column_length = get_lines_width(matrix)
    return calculate(stars, row_length, column_length)

print(sol_1("data1.txt"))
