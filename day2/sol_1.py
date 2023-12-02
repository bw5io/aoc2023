import aoc_lib

def parse(line):
    max_cubes = {}
    first_parse = line.split(":")
    game_number = int(first_parse[0].split(" ")[1])
    rounds = first_parse[1].split(";")
    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            cube_no_empty = [x for x in cube.split(" ") if x]
            cube_count, cube_color = int(cube_no_empty[0]), cube_no_empty[1]
            if cube_color in max_cubes:
                max_cubes[cube_color] = max(cube_count, max_cubes[cube_color])
            else:
                max_cubes[cube_color] = cube_count
    return game_number, max_cubes


def sol_1(input):
    input_list = aoc_lib.file_to_array(input)
    possible_list = []
    configuration = {"red": 12, "green": 13, "blue": 14}
    for i in input_list:
        if len(i)<2:
            continue
        current_game, cubes = parse(i)
        flag_valid = True
        for color, number in cubes.items():
            if number > configuration[color]:
                flag_valid = False
                break
        if flag_valid == True:
            possible_list.append(current_game)
    return sum(possible_list)


print(sol_1("test1.txt"))
print(sol_1("data.txt"))