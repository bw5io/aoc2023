def hash(to_be_encoded):
    hashed_value = 0
    for i in list(to_be_encoded):
        hashed_value+=ord(i)
        hashed_value*=17
        hashed_value=hashed_value%256
    return hashed_value

def sol_1(filename):
    openedfile=open(filename)
    to_be_hashed = openedfile.readline().strip().split(",")
    answers=[]
    for i in to_be_hashed:
        answers.append(hash(i))
    return sum(answers)

print(sol_1("data.txt"))