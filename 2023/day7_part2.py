file = open('input.txt', 'r')
content = file.readlines()
file.close()

res = 0

hands = []
bids = []

number = ''
bid = ''
for line in content:
    for ch in line:
        if ch != ' ' and ch != '\n':
            if ch == 'A':
                number += 'E'
            elif ch == 'K':
                number += 'D'
            elif ch == 'Q':
                number += 'C'
            elif ch == 'J':
                number += '1'
            elif ch == 'T':
                number += 'A'
            else:
                number += ch
        else:
            if len(hands) == len(bids):
                hands.append(number)
            else:
                bids.append(int(number))
            number = ''
if number != '':
    bids.append(int(number))

hands = zip(hands, bids)

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
pair = []
high_card = []

trips_counter = 0
pair_counter = 0

for hand in hands:
    for ch in hand[0]:
        if hand[0].count(ch) == 5:
            five_kind.append(hand)
            break
        elif hand[0].count(ch) == 4:
            if "1" in hand[0]:
                five_kind.append(hand)
            else:
                four_kind.append(hand)
            break
        elif hand[0].count(ch) == 3:
            trips_counter += 1
        elif hand[0].count(ch) == 2:
            pair_counter += 1

    if hand not in five_kind and hand not in four_kind:
        if trips_counter == 3 and pair_counter == 2:
            if "1" in hand[0]:
                five_kind.append(hand)
            else:
                full_house.append(hand)
        elif trips_counter == 3 and pair_counter == 0:
            if "1" in hand[0]:
                four_kind.append(hand)
            else:
                three_kind.append(hand)
        elif pair_counter == 4:
            if hand[0].count('1') == 2:
                four_kind.append(hand)
            elif hand[0].count('1') == 1:
                full_house.append(hand)
            else:
                two_pair.append(hand)
        elif trips_counter == 0 and pair_counter == 2:
            if "1" in hand[0]:
                three_kind.append(hand)
            else:
                pair.append(hand)
        else:
            if "1" in hand[0]:
                pair.append(hand)
            else:
                high_card.append(hand)

    trips_counter = pair_counter = 0

five_kind = sorted(five_kind)
four_kind = sorted(four_kind)
full_house = sorted(full_house)
three_kind = sorted(three_kind)
two_pair = sorted(two_pair)
pair = sorted(pair)
high_card = sorted(high_card)

for i, hand in enumerate(high_card):
    res += hand[1] * (i + 1)

for i, hand in enumerate(pair):
    res += hand[1] * (i + 1 + len(high_card))

for i, hand in enumerate(two_pair):
    res += hand[1] * (i + 1 + len(high_card) + len(pair))

for i, hand in enumerate(three_kind):
    res += hand[1] * (i + 1 + len(high_card) + len(pair) + len(two_pair))

for i, hand in enumerate(full_house):
    res += hand[1] * (i + 1 + len(high_card) + len(pair) + len(two_pair) + len(three_kind))

for i, hand in enumerate(four_kind):
    res += hand[1] * (i + 1 + len(high_card) + len(pair) + len(two_pair) + len(three_kind) + len(full_house))

for i, hand in enumerate(five_kind):
    res += hand[1] * (i + 1 + len(high_card) + len(pair) + len(two_pair) + len(three_kind) + len(full_house) + len(four_kind))

print(res)
