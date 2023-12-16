def hash(to_be_encoded):
    hashed_value = 0
    for i in list(to_be_encoded):
        hashed_value+=ord(i)
        hashed_value*=17
        hashed_value=hashed_value%256
    return hashed_value

def sol_1(filename):
    openedfile=open(filename)
    instructions = openedfile.readline().strip().split(",")
    box_map = {}
    for i in instructions:
        if "=" in i:
            instruction = i.split("=")
            label = instruction[0]
            lens = instruction[1]
            box = hash(label)
            if box in box_map:
                box_map[box][label]=lens
            else:
                box_map[box]={label: lens}
        if "-" in i:
            label = i.replace("-","")
            box = hash(label)
            if box in box_map and label in box_map[box]:
                    box_map[box].pop(label)
    answer = 0
    for k, v in box_map.items():
        box_power = k+1
        box_labels = list(v.keys())
        for i in range(len(box_labels)):
            sequence_power = i+1
            lens = v[box_labels[i]]
            answer += box_power * sequence_power * int(lens)
    return answer

print(sol_1("data.txt"))