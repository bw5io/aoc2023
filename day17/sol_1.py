import aoc_lib
import sys
from dataclasses import dataclass
sys.setrecursionlimit(10000000)
direction_dict = {
  'S': (0, 1),
  'N': (0, -1),
  'W': (-1, 0),
  'E': (1, 0)
}

opposite_direction = {
    'S': 'N',
    'N': 'S',
    'W': 'E',
    'E': 'W'
}

@dataclass
class next_step():
    x: int
    y: int
    direction: str
    direction_steps: int

    def get_location(self):
        return f"{self.x},{self.y}"
    
    def get_distance(self, track_record):
        return track_record[self.y][self.x][f"{self.direction}{self.direction_steps}"]
    
    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, direction: {self.direction}, steps: {self.direction_steps}"

def find_a_way(matrix, track_record, init_x, init_y):
    new_steps = [next_step(init_x, init_y, 'E', 0)]
    while new_steps:
        this_steps = [new_steps.pop(0)]
        while new_steps and new_steps[0].get_distance(track_record)==this_steps[0].get_distance(track_record):
            this_steps.append(new_steps.pop(0))
        for this_step in this_steps:
            if this_step.x == len(matrix[this_step.y])-1 and this_step.y == len(matrix)-1:
                return this_step.get_distance(track_record)
            new_directions = ['S', 'N', 'W', 'E']
            new_directions.remove(opposite_direction[this_step.direction])
            if this_step.direction_steps >= 3:
                new_directions.remove(this_step.direction)
            for new_direction in new_directions:
                new_direction_steps = this_step.direction_steps+1 if new_direction == this_step.direction else 1
                step_x, step_y = direction_dict[new_direction]
                new_x = this_step.x+step_x
                new_y = this_step.y+step_y
                if new_y in range(len(matrix)) and new_x in range(len(matrix[new_y])):
                    if track_record[new_y][new_x][f"{new_direction}{new_direction_steps}"] == -1:
                        track_record[new_y][new_x][f"{new_direction}{new_direction_steps}"] = this_step.get_distance(track_record)+matrix[new_y][new_x]
                        new_steps.append(next_step(new_x, new_y, new_direction, new_direction_steps))
        new_steps.sort(key=lambda x: x.get_distance(track_record))    

def parse(input_list):
    current_matrix = []
    for i in input_list:
        if i=="":
            break
        else:
            current_matrix.append([int(j) for j in list(i)])
    return current_matrix

def create_empty_matrix(matrix):
    empty_matrix = []
    for i in matrix:
        empty_row = []
        for _ in i:
            empty_row.append({
                "E1": -1,
                "E2": -1,
                "E3": -1,
                "W1": -1,
                "W2": -1,
                "W3": -1,
                "S1": -1,
                "S2": -1,
                "S3": -1,
                "N1": -1,
                "N2": -1,
                "N3": -1
            })
        empty_matrix.append(empty_row)
    # print(empty_matrix)
    empty_matrix[0][0]={
        "E0": 0,
        "W0": 0,
        "S0": 0,
        "N0": 0,
        "E1": -1,
        "E2": -1,
        "E3": -1,
        "W1": -1,
        "W2": -1,
        "W3": -1,
        "S1": -1,
        "S2": -1,
        "S3": -1,
        "N1": -1,
        "N2": -1,
        "N3": -1
    }
    return empty_matrix

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    matrix = parse(input_list)
    empty_matrix = create_empty_matrix(matrix)
    answer = find_a_way(matrix, empty_matrix, 0,  0)
    return answer

print(sol_1("data.txt"))
