import aoc_lib
from dataclasses import dataclass
from typing import Union
from copy import deepcopy

@dataclass
class instruction():
    category: str
    threshold: int
    direction: str

    true_outcome: str
    false_outcome: str

    def __repr__(self):
        return f"<criteria: category: {self.category}, threshold: {self.threshold}, direction: {self.direction}, true_outcome: {self.true_outcome}, false_outcome: {self.false_outcome}>"

    def report_range(self, range_size=4000, existing_ranges={}):
        if self.category not in existing_ranges:
            existing_ranges[self.category] = [(1,range_size)]
        true_range, false_range = [], []
        for existing_range in existing_ranges[self.category]:
            if self.threshold in range(existing_range[0], existing_range[1]+1):
                if self.direction == ">":
                    true_range.append((self.threshold+1, existing_range[1]))
                    false_range.append((existing_range[0], self.threshold))
                else:
                    false_range.append((self.threshold, existing_range[1]))
                    true_range.append((existing_range[0], self.threshold-1))
            else: 
                if (self.direction == ">" and existing_range[0] > self.threshold) or self.direction =="<" and existing_range[1] < self.threshold:
                    true_range.append(existing_range)
                else:
                    false_range.append(false_range)
        new_true_ranges = deepcopy(existing_ranges)
        new_false_ranges = deepcopy(existing_ranges)
        new_true_ranges[self.category] = true_range
        new_false_ranges[self.category] = false_range
        return new_true_ranges, new_false_ranges

def parse_statement(name, statement):
    instructions = {}
    print(name, statement)
    first_parse = statement.split(":",1)
    category=first_parse[0][0]
    direction=first_parse[0][1]
    threshold=int(first_parse[0][2:])
    second_parse=first_parse[1].split(",",1)
    true_outcome = second_parse[0]
    if ":" in second_parse[1]:
        instructions = parse_statement(name+"sub", second_parse[1])
        second_parse[1] = name+"sub"
    false_outcome = second_parse[1]
    instructions[name]=instruction(category, threshold, direction, true_outcome, false_outcome)
    return instructions

def parse(input_list):
    instructions, parts = {}, []
    instructions_flag = True
    for i in input_list:
        if instructions_flag == True:
            if i=="":
                instructions_flag = False
                break
            else:
                i=i.replace("}", "")
            first_parse = i.split("{")
            name = first_parse[0]
            next_parse = first_parse[1]
            instructions = instructions | parse_statement(name, next_parse)
            continue
    return instructions

def build_pool(instructions, max_quality=4000):
    stack_list = ["in"]
    out_range = {}
    while stack_list:
        # print(stack_list)
        this_round = stack_list.pop(0)
        # print(this_round, instructions[this_round])
        if instructions[this_round].true_outcome not in ["A", "R"]:
            if instructions[this_round].true_outcome not in stack_list:
                stack_list.append(instructions[this_round].true_outcome)
        if instructions[this_round].false_outcome not in ["A", "R"]:
            if instructions[this_round].false_outcome not in stack_list:
                stack_list.append(instructions[this_round].false_outcome)
        if this_round not in out_range:
            out_range[this_round]=[{}]
        while out_range[this_round]:
            this_range=out_range[this_round].pop()
            # print(this_range)
            true_range, false_range = instructions[this_round].report_range(existing_ranges = this_range)
            if instructions[this_round].true_outcome not in out_range:
                out_range[instructions[this_round].true_outcome]=[]
            if instructions[this_round].false_outcome not in out_range:
                out_range[instructions[this_round].false_outcome]=[]
            out_range[instructions[this_round].true_outcome].append(true_range)
            out_range[instructions[this_round].false_outcome].append(false_range)
            # print(true_range, false_range)
    return out_range


    print(out_range)
    return out_range

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    instructions = (parse(input_list))
    out_range = build_pool(instructions)
    answer = 0
    for each_criteria in out_range["A"]:
        count = 1
        for j in ["x", "m", "a", "s"]:
            if j in each_criteria:
                current_category=0
                for k in each_criteria[j]:
                    current_category+=k[1]-k[0]+1
                count *= current_category
            else:
                count *= 4000
        answer+=count
    return answer
    # for i in instructions:
    #     print(i, instructions[i])
    # build_pool(instructions)
    # for part in parts:
    #     outcome += part.evaluate(instructions)
    # return outcome

print(sol_1("data.txt"))