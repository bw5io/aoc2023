import aoc_lib

def parse(input_list):
    seeds = []
    rule_sets = []
    seeds_line=input_list.pop(0)
    input_list.pop(0)
    seeds=[int(x) for x in seeds_line.split(" ")[1:]]
    new_step_flag = True
    rules=[]
    for line in input_list:
        if new_step_flag == True:
            new_step_flag = False
            continue
        if line=="":
            rule_sets.append(rules)
            rules=[]
            new_step_flag = True
            continue
        rules.append([int(x) for x in line.split(" ")])
    return seeds, rule_sets

def run_rules(seeds_range, rules):
    new_seeds_range=[]
    for i in range(len(seeds_range)):
        this_seeds_range = [[seeds_range[i][0], seeds_range[i][1]]]
        for rule in rules:
            for i in this_seeds_range:
                if i[1] < rule[1] or i[0] > rule[1]+rule[2]-1:
                    continue
                elif i[0] >= rule[1] and i[1] <= rule[1]+rule[2]-1:
                    new_seeds_range.append([i[0]-rule[1]+rule[0],i[1]-rule[1]+rule[0]])
                    this_seeds_range = []
                elif i[0] < rule[1] and i[1] > rule[1]+rule[2]-1:
                    new_seeds_range.append([rule[0], rule[0]+rule[2]-1])
                    this_seeds_range = []
                    this_seeds_range.append([i[0], rule[1]-1])
                    this_seeds_range.append([rule[1]+rule[2], i[1]])
                elif i[0] < rule[1] and i[1] <= rule[1]+rule[2]-1:
                    new_seeds_range.append([rule[0], i[1]-rule[1]+rule[0]])
                    this_seeds_range=[[i[0], rule[1]-1]]
                elif i[0] >= rule[1] and i[1] > rule[1]+rule[2]-1:
                    new_seeds_range.append([i[0]-rule[1]+rule[0], rule[0]+rule[2]-1])
                    this_seeds_range=[[rule[1]+rule[2], i[1]]]
        if len(this_seeds_range)!=0:
            new_seeds_range+=this_seeds_range
    return new_seeds_range

def parse_seeds(input_list):
    seeds_range_list = []
    seeds_range = []
    flag = False
    for i in input_list:
        if flag == True:
            seeds_range.append(seeds_range[0]+i-1)
            seeds_range_list.append(seeds_range)
            seeds_range = []
            flag = False
        else:
            seeds_range.append(i)
            flag = True
    return seeds_range_list
    


def sol_2(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    seeds_init, rule_sets = parse(input_list)
    seeds_range_list = parse_seeds(seeds_init)
    for rules in rule_sets:
        seeds_range_list = run_rules(seeds_range_list, rules)
    return min([i[0] for i in seeds_range_list])

print(sol_2("data1.txt"))