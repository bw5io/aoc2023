import aoc_lib
from collections import Counter

class Card:
    def __init__(self, card_value, bets):
        self.card_value = card_value
        self.card_type = check_card_type(self.card_value)
        self.bets = bets
    
    def __repr__(self):
        return f"Card Value: {self.card_value}, Card Type: {self.card_type}, Bets: {self.bets}"

def check_card_type(card):
    card_count = Counter(str(card))
    card_count_occurence = Counter(card_count.values())
    if 5 in card_count_occurence.keys():
        return 6
    if 4 in card_count_occurence.keys():
        return 5
    if 3 in card_count_occurence.keys():
        if 2 in card_count_occurence.keys():
            return 4
        else:
            return 3
    if 2 in card_count_occurence.keys():
        if card_count_occurence[2]==2:
            return 2
        else:
            return 1
    return 0

def parse(input_list):
    card_on_hand = []
    for line in input_list:
        if line == "":
            break
        line_break = line.split(" ")
        card_on_hand.append(Card(line_break[0], int(line_break[1])))
    return card_on_hand

def compare_right_bigger_than_left(left: Card, right: Card):
    card_map = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "1": 1,
    }
    if left.card_type > right.card_type:
        return False
    if left.card_type < right.card_type:
        return True
    count = 0
    left_card_value = list(left.card_value)
    right_card_value = list(right.card_value)
    while count < len(left_card_value):
        if card_map[left_card_value[count]] < card_map[right_card_value[count]]:
            return True
        if card_map[left_card_value[count]] > card_map[right_card_value[count]]:
            return False
        count+=1
    return False


def sort(card_on_hand):
    if len(card_on_hand)<=1:
        return card_on_hand
    left = []
    right = []
    middle = card_on_hand[0]
    for i in range(1, len(card_on_hand)):
        if compare_right_bigger_than_left(middle, card_on_hand[i]):
            right.append(card_on_hand[i])
        else:
            left.append(card_on_hand[i])
    return sort(left)+[middle]+sort(right)
    

def sol_1(input_file):
    input_list = aoc_lib.file_to_array(input_file)
    card_on_hand = parse(input_list)
    sorted_card_on_hand = sort(card_on_hand)
    return sum([(i+1)*sorted_card_on_hand[i].bets for i in range(len(sorted_card_on_hand))])

# check_card_type("33444")

print(sol_1("data1.txt"))