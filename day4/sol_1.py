import aoc_lib

def parse(cards):
    parsed_cards = []
    for card in cards:
        if card == "":
            break
        first_parse = card.split("|")
        on_hand = list(int(x) for x in first_parse[1].split(" ") if x!="")
        second_parse = first_parse[0].split(":")
        winning_numbers = list(int(x) for x in second_parse[1].split(" ") if x!="")
        parsed_cards.append((on_hand, winning_numbers))
    return parsed_cards

def check_card(winning_numbers, on_hand):
    points = 0
    for i in on_hand:
        if i in winning_numbers:
            if points ==0:
                points = 1
            else:
                points *=2
    return points


def sol_1(input):
    input_list = aoc_lib.file_to_array(input)
    cards = parse(input_list)
    points = []
    for on_hand, winning_numbers in cards:
        points.append(check_card(winning_numbers, on_hand))
    print(points)
    return sum(points)

print(sol_1("data1.txt"))