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

def run_rules(seeds, rules):
    for i in range(len(seeds)):
        for rule in rules:
            if seeds[i] in range(rule[1], rule[1]+rule[2]):
                seeds[i] = seeds[i]-rule[1]+rule[0]
                break
    return seeds


def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    seeds, rule_sets = parse(input_list)
    # print(seeds, rule_sets)
    for rules in rule_sets:
        seeds = run_rules(seeds, rules)
        # print(seeds, rules)
    return min(seeds)

print(sol_1("data1.txt"))