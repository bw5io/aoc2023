import aoc_lib
from dataclasses import dataclass
from typing import Union

@dataclass
class machine_part():
    x: int
    m: int
    a: int
    s: int

    def __repr__(self):
        return f"<machine_part: x: {self.x}, m: {self.m}, a: {self.a}, s: {self.s}, ratings: {self.ratings()}>"
    
    def __add__(self, a):
        return self.x + self.m + self.a + self.s + a
    
    def __radd__(self, a):
        return a + self.x + self.m + self.a + self.s
    
    def ratings(self):
        return self.x + self.m + self.a + self.s
    
    def evaluate(self, instructions):
        current_instruction = "in"
        outcome = ""
        while outcome not in ["A", "R"]:
            outcome = instructions[current_instruction].evaluate(self)
            current_instruction = outcome
        if outcome=="A":
            return self.ratings()
        if outcome=="R":
            return 0

@dataclass
class instruction():
    category: str
    threshold: int
    direction: str

    true_outcome: str
    false_outcome: Union[str, 'instruction']

    def evaluate(self, part: machine_part):
        inspected_number = 0
        outcome = False
        match self.category:
            case "x":
                inspected_number = part.x
            case "m":
                inspected_number = part.m
            case "a":
                inspected_number = part.a
            case "s":
                inspected_number = part.s
        match self.direction:
            case ">":
                outcome = inspected_number > self.threshold
            case "<":
                outcome = inspected_number < self.threshold
        match outcome:
            case True:
                return self.true_outcome
            case False:
                return self.false_outcome if type(self.false_outcome) is str else self.false_outcome.evaluate(part)

    def __repr__(self):
        return f"<criteria: category: {self.category}, threshold: {self.threshold}, direction: {self.direction}, true_outcome: {self.true_outcome}, false_outcome: {self.false_outcome}>"

def parse_statement(statement):
    first_parse = statement.split(":",1)
    category=first_parse[0][0]
    direction=first_parse[0][1]
    threshold=int(first_parse[0][2:])
    second_parse=first_parse[1].split(",",1)
    true_outcome = second_parse[0]
    false_outcome = second_parse[1] if ":" not in second_parse[1] else parse_statement(second_parse[1])
    return instruction(category, threshold, direction, true_outcome, false_outcome)

def parse(input_list):
    instructions, parts = {}, []
    instructions_flag = True
    for i in input_list:
        if instructions_flag == True:
            if i=="":
                instructions_flag = False
                continue
            else:
                i=i.replace("}", "")
            first_parse = i.split("{")
            name = first_parse[0]
            next_parse = first_parse[1]
            instructions[name]=parse_statement(next_parse)
            continue
        if i=="":
            break
        i=i.replace("{", "")
        i=i.replace("}", "")
        first_parse = i.split(",")
        this_object = {}
        for j in first_parse:
            this_object[j.split("=")[0]]=int(j.split("=")[1])
        parts.append(machine_part(this_object["x"], this_object["m"], this_object["a"], this_object["s"]))
    return instructions, parts

def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    instructions, parts = (parse(input_list))
    outcome = 0
    for part in parts:
        outcome += part.evaluate(instructions)
    return outcome

print(sol_1("data.txt"))