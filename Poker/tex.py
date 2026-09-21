#CSIT 163 SP OL1
#2/27/26
#proj06
#Wyatt Robertson



import cards

deck = cards.Deck()
deck.shuffle()

print(deck)


hand1_list = []
hand2_list = []
foundation_list = []
for i in range(2):
    hand1_list.append(deck.deal())
    hand2_list.append(deck.deal())

for i in range(5) :
    foundation_list.append(deck.deal())

print(hand1_list , "\n")
print(hand2_list , "\n")
print(foundation_list , "\n")
print(deck)

possible_hand1 = hand1_list + foundation_list
possible_hand2 = hand2_list + foundation_list

card1 = hand1_list[0]
card2 = hand1_list[1]

card3 = hand2_list[0]
card4 = hand2_list[1]

card5 = foundation_list[0]
card6 = foundation_list[1]
card7 = foundation_list[2]
card8 = foundation_list[3]
card9 = foundation_list[4]


def rank_dict(hand) :
    rdict = {}
    for x in range(7) :
        rank = str((hand)[x]).split('-')[0]


        suit = list(str((hand)[x]).split('-')[1])


        if rank in rdict:
            rdict[rank] = rdict[rank] + suit
        else:
            rdict[rank] = suit

    return rdict
print(rank_dict(possible_hand1))
print(rank_dict(possible_hand2))
