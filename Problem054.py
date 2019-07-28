# Finding the most common element in a list
def most_common(lst):
    return max(set(lst), key=lst.count)


def get_highest_card(hand):
    aux = [card[0] for card in hand]
    order = ['A', 'K', 'Q', 'J', 'T'] + [str(i) for i in range(9, 1, -1)]
    for i in range(len(order)):
        if order[i] in aux:
            return order[i]


def is_flush(hand):
    return [len(set(card[1] for card in hand)) == 1, get_highest_card(hand)]


def is_royal_flush(hand):
    return [set([card[0] for card in hand]) == {'T', 'J', 'Q', 'K', 'A'} and is_flush(hand)[0]]


def is_straight(hand):
    order = ['A', 'K', 'Q', 'J', 'T'] + [str(i) for i in range(9, 1, -1)]
    idx = set([order.index(i[0]) for i in hand])
    return [max(idx) - min(idx) == 4 and len(idx) == 5, get_highest_card(hand)]


def is_one_pair(hand):
    aux = [card[0] for card in hand]
    return [len(set(aux)) == 4, most_common(aux)]


def is_two_pairs(hand):
    aux1 = [card[0] for card in hand]
    aux2 = [card[0] for card in hand]
    for c in set(aux1):
        aux2.remove(c)
    return [len(set(aux1)) == 3 and aux1.count(most_common(aux1)) == 2, get_highest_card(aux2)]


def is_three_of_a_kind(hand):
    aux = [card[0] for card in hand]
    return [len(set(aux)) == 3 and aux.count(most_common(aux)) == 3, most_common(aux)]


def is_four_of_a_kind(hand):
    aux = [card[0] for card in hand]
    return [len(set(aux)) == 2 and aux.count(most_common(aux)) == 4, most_common(aux)]


def is_full_house(hand):
    aux = [card[0] for card in hand]
    return [len(set(aux)) == 2 and aux.count(most_common(aux)) == 3, most_common(aux)]


def is_straight_flush(hand):
    return [is_straight(hand)[0] and len(set(card[1] for card in hand)) == 1, get_highest_card(hand)]


# From 1 to 10 evaluate the strength of a hand
def get_hand_strength(hand):
    if is_royal_flush(hand)[0]:
        return [10]
    str_fl = is_straight_flush(hand)
    if str_fl[0]:
        return [9, str_fl[1]]
    foak = is_four_of_a_kind(hand)
    if foak[0]:
        return [8, foak[1]]
    fh = is_full_house(hand)
    if fh[0]:
        return [7, fh[1]]
    flsh = is_flush(hand)
    if flsh[0]:
        return [6, flsh[1]]
    strt = is_straight(hand)
    if strt[0]:
        return [5, strt[1]]
    toak = is_three_of_a_kind(hand)
    if toak[0]:
        return [4, toak[1]]
    tp = is_two_pairs(hand)
    if tp[0]:
        return [3, tp[1]]
    op = is_one_pair(hand)
    if op[0]:
        return [2, op[1]]
    return [1, get_highest_card(hand)]


# Return 1 if player 1 wins and 0 otherwise
def play_poker(hand_1, hand_2):
    player_1 = get_hand_strength(hand_1)
    player_2 = get_hand_strength(hand_2)
    if player_1[0] > player_2[0]:
        return 1
    elif player_1[0] == player_2[0] == 2 and player_1[1] == player_2[1]:
        return get_highest_card([hand_1, hand_2]) == get_highest_card(hand_1)
    elif player_1[0] == player_2[0] and get_highest_card([player_1[1], player_2[1]]) == player_1[1]:
        return 1
    else:
        return 0


# Count the number of victories of player 1 in 'hs'
def count_player1_wins(hs):
    s = 0
    for h in hs:
        hand_1 = h[0:4 * 3 + 2].split(' ')
        hand_2 = h[4 * 3 + 3:].split(' ')
        s += play_poker(hand_1, hand_2) == 1
    return s


with open('p054_poker.txt') as f:
    hands = f.read()
hands = hands.split('\n')
hands.pop(len(hands) - 1)
print(count_player1_wins(hands))
