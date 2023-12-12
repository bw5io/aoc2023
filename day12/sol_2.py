import aoc_lib
from functools import cache, reduce
from dataclasses import asdict, dataclass, field

@dataclass(frozen=True)
class SpringRecord():
    record: str
    pattern: tuple

    @cache
    def brute_force(this, cur_position, cur_pattern, cur_group_position, on_pool_flag=False):
        # print(this.record, this.pattern, cur_position, cur_pattern, cur_group_position, on_pool_flag)
        if cur_pattern==len(this.pattern):
            if this.record[cur_position:].count("#")==0:
                return 1
            return 0
        if cur_position==len(this.record):
            if cur_pattern==len(this.pattern):
                return 1
            if cur_pattern==len(this.pattern)-1 and cur_group_position==this.pattern[cur_pattern]:
                return 1
            return 0
        possibility=["#", "."]
        possible_solutions=0
        if this.record[cur_position]!="?":
            if this.record[cur_position]=="#":
                cur_group_position+=1
                on_pool_flag=True
            if this.record[cur_position]==".":
                if on_pool_flag==True:
                    if this.pattern[cur_pattern]!=cur_group_position:
                        return 0
                    cur_pattern+=1
                    cur_group_position=0
                    on_pool_flag=False
            possible_solutions+=this.brute_force(cur_position+1, cur_pattern, cur_group_position, on_pool_flag)
        else:
            possible_solutions+=this.brute_force(cur_position+1, cur_pattern, cur_group_position+1, True)
            if on_pool_flag==True:
                if this.pattern[cur_pattern]!=cur_group_position:
                    return possible_solutions
                possible_solutions+=this.brute_force(cur_position+1, cur_pattern+1, 0, False)
            else: 
                possible_solutions+=this.brute_force(cur_position+1, cur_pattern, cur_group_position, False)
        return possible_solutions

    def unfold(this):
        new_rec = "?".join([this.record]*5)
        new_pattern = this.pattern*5
        return SpringRecord(new_rec, new_pattern)

def parse(text_list):
    springs = []
    for i in text_list:
        if len(i)==0:
            continue
        spring = i.split(" ")[0]
        pattern_text = i.split(" ")[1]
        pattern = tuple(int(j) for j in pattern_text.split(","))
        springs.append(SpringRecord(spring, pattern))
    return springs



def sol_1(text_file):
    input_list = aoc_lib.file_to_array(text_file)
    springs = parse(input_list)
    valid_possibilities = 0
    for i in springs:
        k=i.unfold()
        current_possibility = k.brute_force(0, 0, 0)
        print(i, current_possibility)
        valid_possibilities+=current_possibility
    return valid_possibilities

print(sol_1("data.txt"))