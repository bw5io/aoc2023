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
        parsed_cards.append({"on_hand": on_hand, "winning_numbers": winning_numbers, "copies": 1})
    return parsed_cards

def check_card(cards, i):
    points = 0
    on_hand = cards[i]["on_hand"]
    winning_numbers = cards[i]["winning_numbers"]
    for j in on_hand:
        if j in winning_numbers:
            points += 1
    for j in range(1,points+1):
        try:
            cards[i+j]["copies"]+=cards[i]["copies"]
            print(cards[i+j])
        except:
            pass
    return cards


def sol_2(input):
    input_list = aoc_lib.file_to_array(input)
    cards = parse(input_list)
    points = []
    print(cards)
    for i in range(len(cards)):
        cards = check_card(cards, i)
    print(cards)
    return sum(card["copies"] for card in cards)

print(sol_2("data1.txt"))