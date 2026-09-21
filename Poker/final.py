#CSIT 163 SP OL1
#2/27/26
#proj06
#Wyatt Robertson



import cards

deck = cards.Deck()
deck.shuffle()


while deck >= 9:
    hand1_list = []
    hand2_list = []
    foundation_list = []
    for i in range(2):
        hand1_list.append(deck.deal())
        hand2_list.append(deck.deal())

    for i in range(5) :
        foundation_list.append(deck.deal())



    hand1_list[0] = 'A-C'
    hand1_list[1] = '2-D'

    hand2_list[0] = '10-S'
    hand2_list[1] = '7-D'

    foundation_list[0] = '6-S'
    foundation_list[1] = 'J-H'
    foundation_list[2] = 'Q-S'
    foundation_list[3] = '3-C'
    foundation_list[4] = '4-H'

    print("player 1's hand is" , hand1_list , "\n")
    print("player 2's hand is" , hand2_list , "\n")
    print("the foundation is" , foundation_list , "\n")

    possible_hand1 = hand1_list + foundation_list
    possible_hand2 = hand2_list + foundation_list



    def rank_dict(hand) :
        rdict = {}
        for x in range(7) :
            rank = str((hand)[x]).split('-')[0]
            if rank == 'Q' :
                rank = 12
            if rank == 'K' :
                rank = 13
            if rank == 'A' :
                rank = 14
            if rank == 'J' :
                rank = 11
            else:
                rank = int(rank)


            suit = list(str((hand)[x]).split('-')[1])


            if rank in rdict:
                rdict[rank] = rdict[rank] + suit
            else:
                rdict[rank] = suit

        return rdict


    def suit_dict(hand) :
        sdict = {}
        for x in range(7) :
            prank = str((hand)[x]).split('-')[0]
            rank = [prank]

            suit = str((hand)[x]).split('-')[1]


            if suit in sdict:
                sdict[suit] = sdict[suit] + rank
            else:
                sdict[suit] = rank

        return sdict








    def straight_flush(hand) :
        empty_list = []
        if 'H' in suit_dict(hand) :
            if len(suit_dict(hand)['H']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'H' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue


                z = 0
                value_list = []
                while z < len(empty_list):
                    empty_list.sort()
                    if empty_list[z][0] == 'Q' :
                        value = 12
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'K' :
                        value = 13
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'A' :
                        value = 14
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'J' :
                        value = 11
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0:2] == '10' :
                        value = 10
                        z += 1
                        value_list.append(value)
                        continue
                    else:
                        value = int(empty_list[z][0])
                        z += 1
                        value_list.append(value)
                        continue

                value_list.sort()
                while len(value_list) > 5:
                    if value_list[0] + 3 != value_list[3]  and value_list[0] + 2 != value_list[2]:
                        value_list.pop(0)
                        continue
                    if value_list[len(value_list)-1] - 2 != value_list[len(value_list) - 3] and value_list[len(value_list)-2] - 2 != value_list[len(value_list) - 4]:
                        value_list.pop()
                        continue


                if value_list[0] + 1 == value_list[1] and value_list[1] + 1 == value_list[2] and value_list[2] + 1 == value_list[3] and value_list[3] + 1 == value_list[4]:


                    winning_hand = []
                    x = 0
                    while x <= 4 :
                        if int(value_list[x]) == 11 :
                            value_list[x] = 'J'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 12 :
                            value_list[x] = 'Q'
                            str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 13 :
                            value_list[x] = 'K'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 14 :
                            value_list[x] = 'A'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 10 :
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+4])
                            x += 1
                            continue
                        else :
                            value_list[x] = int(value_list[x])
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue

                    return f'{winning_hand}, which is a straight flush.'
        if 'S' in suit_dict(hand) :
            if len(suit_dict(hand)['S']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'S' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue


                z = 0
                value_list = []
                while z < len(empty_list):
                    empty_list.sort()
                    if empty_list[z][0] == 'Q' :
                        value = 12
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'K' :
                        value = 13
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'A' :
                        value = 14
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'J' :
                        value = 11
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0:2] == '10' :
                        value = 10
                        z += 1
                        value_list.append(value)
                        continue
                    else:
                        value = int(empty_list[z][0])
                        z += 1
                        value_list.append(value)
                        continue

                value_list.sort()
                while len(value_list) > 5:
                    if value_list[0] + 3 != value_list[3]  and value_list[0] + 2 != value_list[2]:
                        value_list.pop(0)
                        continue
                    if value_list[len(value_list)-1] - 2 != value_list[len(value_list) - 3] and value_list[len(value_list)-2] - 2 != value_list[len(value_list) - 4]:
                        value_list.pop()
                        continue


                if value_list[0] + 1 == value_list[1] and value_list[1] + 1 == value_list[2] and value_list[2] + 1 == value_list[3] and value_list[3] + 1 == value_list[4]:


                    winning_hand = []
                    x = 0
                    while x <= 4 :
                        if int(value_list[x]) == 11 :
                            value_list[x] = 'J'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 12 :
                            value_list[x] = 'Q'
                            str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 13 :
                            value_list[x] = 'K'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 14 :
                            value_list[x] = 'A'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 10 :
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+4])
                            x += 1
                            continue
                        else :
                            value_list[x] = int(value_list[x])
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                    return f'{winning_hand}, which is a straight flush.'

        if 'C' in suit_dict(hand) :
            if len(suit_dict(hand)['C']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'C' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue


                z = 0
                value_list = []
                while z < len(empty_list):
                    empty_list.sort()
                    if empty_list[z][0] == 'Q' :
                        value = 12
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'K' :
                        value = 13
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'A' :
                        value = 14
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'J' :
                        value = 11
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0:2] == '10' :
                        value = 10
                        z += 1
                        value_list.append(value)
                        continue
                    else:
                        value = int(empty_list[z][0])
                        z += 1
                        value_list.append(value)
                        continue

                value_list.sort()
                while len(value_list) > 5:
                    if value_list[0] + 3 != value_list[3]  and value_list[0] + 2 != value_list[2]:
                        value_list.pop(0)
                        continue
                    if value_list[len(value_list)-1] - 2 != value_list[len(value_list) - 3] and value_list[len(value_list)-2] - 2 != value_list[len(value_list) - 4]:
                        value_list.pop()
                        continue


                if value_list[0] + 1 == value_list[1] and value_list[1] + 1 == value_list[2] and value_list[2] + 1 == value_list[3] and value_list[3] + 1 == value_list[4]:


                    winning_hand = []
                    x = 0
                    while x <= 4 :
                        if int(value_list[x]) == 11 :
                            value_list[x] = 'J'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 12 :
                            value_list[x] = 'Q'
                            str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 13 :
                            value_list[x] = 'K'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 14 :
                            value_list[x] = 'A'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 10 :
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+4])
                            x += 1
                            continue
                        else :
                            value_list[x] = int(value_list[x])
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                    return f'{winning_hand}, which is a straight flush.'

        if 'D' in suit_dict(hand) :
            if len(suit_dict(hand)['D']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'D' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue


                z = 0
                value_list = []
                while z < len(empty_list):
                    empty_list.sort()
                    if empty_list[z][0] == 'Q' :
                        value = 12
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'K' :
                        value = 13
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'A' :
                        value = 14
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0] == 'J' :
                        value = 11
                        z += 1
                        value_list.append(value)
                        continue
                    if empty_list[z][0:2] == '10' :
                        value = 10
                        z += 1
                        value_list.append(value)
                        continue
                    else:
                        value = int(empty_list[z][0])
                        z += 1
                        value_list.append(value)
                        continue

                value_list.sort()
                while len(value_list) > 5:
                    if value_list[0] + 3 != value_list[3]  and value_list[0] + 2 != value_list[2]:
                        value_list.pop(0)
                        continue
                    if value_list[len(value_list)-1] - 2 != value_list[len(value_list) - 3] and value_list[len(value_list)-2] - 2 != value_list[len(value_list) - 4]:
                        value_list.pop()
                        continue


                if value_list[0] + 1 == value_list[1] and value_list[1] + 1 == value_list[2] and value_list[2] + 1 == value_list[3] and value_list[3] + 1 == value_list[4]:


                    winning_hand = []
                    x = 0
                    while x <= 4 :
                        if int(value_list[x]) == 11 :
                            value_list[x] = 'J'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 12 :
                            value_list[x] = 'Q'
                            str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 13 :
                            value_list[x] = 'K'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 14 :
                            value_list[x] = 'A'
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                        if value_list[x] == 10 :
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+4])
                            x += 1
                            continue
                        else :
                            value_list[x] = int(value_list[x])
                            hand = str(hand)
                            winning_hand.append(hand[hand.find(str(value_list[x])):hand.find(str(value_list[x]))+3])
                            x += 1
                            continue
                    return f'{winning_hand}, which is a straight flush.'





    def four_kind(hand) :
        x = 0
        while x < len(list(rank_dict(hand))):
            g = list(rank_dict(hand))[x-1]
            if len(rank_dict(hand)[g]) == 4:
                if g == 14:
                    g = 'A'
                if g == 13:
                    g = 'K'
                if g == 12 :
                    g = 'Q'
                if g == 11 :
                    g = 'J'
                winning_hand = f'{g}-H, {g}-D, {g}-S, {g}-C, which is a four-of-a-kind'
                x += 1
                return winning_hand
            else:
                x += 1

    def full_house(hand) :
        x = 0
        list_format = list(rank_dict(hand))

        while x < len(list_format):
            g = list_format[x-1]
            if len(rank_dict(hand)[g]) >= 3:
                suit1 = rank_dict(hand).pop(g)
                if len(suit1) == 4 :
                    suit1.pop()

                if g == 14:
                    g = 'A'
                if g == 13:
                    g = 'K'
                if g == 12 :
                    g = 'Q'
                if g == 11 :
                    g = 'J'



                list_format.remove(g)


                j = 0
                while j < len(list_format):
                    z = list_format[j-1]
                    if len(rank_dict(hand)[z]) >= 2:
                        suit = rank_dict(hand).pop(z)
                        while len(suit) > 2 :
                            suit.pop()


                        if z == 14:
                            z = 'A'
                        if z == 13:
                            z = 'K'
                        if z == 12 :
                            z = 'Q'
                        if z == 11 :
                            z = 'J'



                        break






                    else:
                        j += 1
                        continue







                if len(rank_dict(hand)[z]) < 2:
                    return None


                winning_hand = f'{g}-{suit1[0]}, {g}-{suit1[1]}, {g}-{suit1[2]}, {z}-{suit[0]}, {z}-{suit[1]}, which is a full house.'
                return winning_hand


            else:
                x += 1
                continue



    def flush(hand) :
        empty_list = []
        if 'H' in suit_dict(hand) :
            if len(suit_dict(hand)['H']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'H' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue

        if 'D' in suit_dict(hand) :
            if len(suit_dict(hand)['D']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'D' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue



        if 'S' in suit_dict(hand) :
            if len(suit_dict(hand)['S']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'S' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue



        if 'C' in suit_dict(hand) :
            if len(suit_dict(hand)['C']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'C' in hand[j] :
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        j += 1
                        continue
        if empty_list == []:
            return None
        return f'{empty_list}, which is a flush'








    def straight(hand):
        y = list(rank_dict(hand))
        y.sort()
        if len(y) == 7:
            if y[2] + 4 != y[6] :
                y.remove(y[6])
            if y[4] -4 != y[0] :
                y.remove(y[0])
        if len(y) == 6:
            if y[1] + 4 != y[5]:
                y.remove(y[5])
            if y[4] - 4 != y[0] :
                y.remove(y[0])
        if len(y) < 5:
            return None
            #You need at least 5 cards to make a straight
        if len(y) > 5:
            y.remove(y[0])
            #checks for 7 card straight and reduces its length to 6 cards if it exists
            if len(y) > 5:
                y.remove(y[0])
                #checks for 6 card straight and reduces its length to 5 cards if it exists




        if len(y) == 5 and y[0] + 1 == y[1] and y[1] + 1 == y[2] and y[2] + 1 == y[3] and y[3] + 1 == y[4]:
            x = 0
            empty_list = []
            stringy = str(hand)
            while x <= 4:
                if y[x] == 14:
                    y[x] = 'A'
                    empty_list.append(stringy[stringy.find(str(y[x])):stringy.find(str(y[x]))+3])
                    x += 1
                    continue
                if y[x] == 13:
                    y[x] = 'K'
                    empty_list.append(stringy[stringy.find(str(y[x])):stringy.find(str(y[x]))+3])
                    x += 1
                    continue
                if y[x] == 12 :
                    y[x] = 'Q'
                    empty_list.append(stringy[stringy.find(str(y[x])):stringy.find(str(y[x]))+3])
                    x += 1
                    continue
                if y[x] == 11 :
                    y[x] = 'J'
                    empty_list.append(stringy[stringy.find(str(y[x])):stringy.find(str(y[x]))+3])
                    x += 1
                    continue


                if y[x] == 10:
                    empty_list.append(stringy[stringy.find(str(y[x])):stringy.find(str(y[x]))+4])
                    x += 1
                    continue

                else:
                    empty_list.append(stringy[stringy.find(str(y[x])):stringy.find(str(y[x]))+3])
                    x += 1
                    continue



            return f'{empty_list}, which is a straight'





        else:
            return None







    def three_kind(hand):
        x = 0
        list_format = list(rank_dict(hand))

        while x < len(list_format):
            g = list_format[x-1]
            if len(rank_dict(hand)[g]) >= 3:
                suit1 = rank_dict(hand).pop(g)
                if len(suit1) == 4 :
                        suit1.pop()

                if g == 14:
                    g = 'A'
                if g == 13:
                    g = 'K'
                if g == 12 :
                    g = 'Q'
                if g == 11 :
                    g = 'J'




                winning_hand = f'{g}-{suit1[0]}, {g}-{suit1[1]}, {g}-{suit1[2]}, which is a three-of-a-kind'

                return winning_hand
            else:
                x += 1
                continue



    def two_pair(hand) :
        x = 0
        list_format = list(rank_dict(hand))

        while x < len(list_format):
            g = list_format[x-1]
            if len(rank_dict(hand)[g]) >= 2:
                suit1 = rank_dict(hand).pop(g)
                while len(suit1) > 2 :
                    suit1.pop()

                if g == 14:
                    g = 'A'
                if g == 13:
                    g = 'K'
                if g == 12 :
                    g = 'Q'
                if g == 11 :
                    g = 'J'



                list_format.remove(g)


                j = 0
                while j < len(list_format):
                    z = list_format[j-1]
                    if len(rank_dict(hand)[z]) >= 2:
                        suit = rank_dict(hand).pop(z)
                        while len(suit) > 2 :
                            suit.pop()


                        if z == 14:
                            z = 'A'
                        if z == 13:
                            z = 'K'
                        if z == 12 :
                            z = 'Q'
                        if z == 11 :
                            z = 'J'

                        break


                    else:
                        j += 1
                        continue



                if len(rank_dict(hand)[z]) < 2:
                    return None


                winning_hand = f'{g}-{suit1[0]}, {g}-{suit1[1]}, {z}-{suit[0]}, {z}-{suit[1]}, which is a two pair'
                return winning_hand


            else:
                x += 1
                continue


    def pair(hand) :
        x = 0
        list_format = list(rank_dict(hand))

        while x < len(list_format):
            g = list_format[x-1]
            if len(rank_dict(hand)[g]) >= 2:
                suit1 = rank_dict(hand).pop(g)
                while len(suit1) > 2 :
                        suit1.pop()

                if g == 14:
                    g = 'A'
                if g == 13:
                    g = 'K'
                if g == 12 :
                    g = 'Q'
                if g == 11 :
                    g = 'J'




                winning_hand = f'{g}-{suit1[0]}, {g}-{suit1[1]}, which is a pair'

                return winning_hand
            else:
                x += 1
                continue

















    #print(straight_flush(possible_hand1))
    #print(straight_flush(possible_hand2))
    #print(four_kind(possible_hand1))
    #print(four_kind(possible_hand2))
    #print(full_house(possible_hand1))
    #print(full_house(possible_hand2))
    #print(flush(possible_hand1))
    #print(flush(possible_hand2))
    #print(straight(possible_hand1))
    #print(straight(possible_hand2))
    #print(three_kind(possible_hand1))
    #print(three_kind(possible_hand2))
    #print(two_pair(possible_hand1))
    #print(two_pair(possible_hand2))
    #print(pair(possible_hand1))
    #print(pair(possible_hand2))
    Checker = 1
    while Checker == 1:
        if straight_flush(possible_hand1) != None and straight_flush(possible_hand2) != None :
            print(f'tie. Player 1 has {straight_flush(possible_hand1)} and player 2 has {straight_flush(possible_hand2)}.')
            break
        elif straight_flush(possible_hand1) != None:
            print(f'Player 1 wins with {straight_flush(possible_hand1)}')
            break
        elif straight_flush(possible_hand2) != None:
            print(f'Player 2 wins with {straight_flush(possible_hand2)}')
            break



        if four_kind(possible_hand1) != None and four_kind(possible_hand2) != None :
            print(f'tie. Player 1 has {four_kind(possible_hand1)} and player 2 has {four_kind(possible_hand2)}.')
            break
        elif four_kind(possible_hand1) != None:
            print(f'Player 1 wins with {four_kind(possible_hand1)}.')
            break
        elif four_kind(possible_hand2) != None:
            print(f'Player 2 wins with {four_kind(possible_hand2)}.')
            break



        if full_house(possible_hand1) != None and full_house(possible_hand2) != None :
            print(f'tie. Player 1 has {full_house(possible_hand1)} and player 2 has {full_house(possible_hand2)}.')
            break
        elif full_house(possible_hand1) != None:
            print(f'Player 1 wins with {full_house(possible_hand1)}.')
            break
        elif full_house(possible_hand2) != None:
            print(f'Player 2 wins with {full_house(possible_hand2)}.')
            break



        if flush(possible_hand1) != None and flush(possible_hand2) != None :
            print(f'tie. Player 1 has {flush(possible_hand1)} and player 2 has {flush(possible_hand2)}.')
            break
        elif flush(possible_hand1) != None:
            print(f'Player 1 wins with {flush(possible_hand1)}.')
            break
        elif flush(possible_hand2) != None:
            print(f'Player 2 wins with {flush(possible_hand2)}.')
            break



        if straight(possible_hand1) != None and straight(possible_hand2) != None :
            print(f'tie. Player 1 has {straight(possible_hand1)} and player 2 has {straight(possible_hand2)}.')
            break
        elif straight(possible_hand1) != None:
            print(f'Player 1 wins with {straight(possible_hand1)}.')
            break
        elif straight(possible_hand2) != None:
            print(f'Player 2 wins with {straight(possible_hand2)}.')
            break



        if three_kind(possible_hand1) != None and three_kind(possible_hand2) != None :
            print(f'tie. Player 1 has {three_kind(possible_hand1)} and player 2 has {three_kind(possible_hand2)}.')
            break
        elif three_kind(possible_hand1) != None:
            print(f'Player 1 wins with {three_kind(possible_hand1)}.')
            break
        elif three_kind(possible_hand2) != None:
            print(f'Player 2 wins with {three_kind(possible_hand2)}.')
            break



        if two_pair(possible_hand1) != None and two_pair(possible_hand2) != None :
            print(f'tie. Player 1 has {two_pair(possible_hand1)} and player 2 has {two_pair(possible_hand2)}.')
            break
        elif two_pair(possible_hand1) != None:
            print(f'Player 1 wins with {two_pair(possible_hand1)}.')
            break
        elif two_pair(possible_hand2) != None:
            print(f'Player 2 wins with {two_pair(possible_hand2)}.')
            break

        if pair(possible_hand1) != None and pair(possible_hand2) != None :
            print(f'tie. Player 1 has {pair(possible_hand1)} and player 2 has {pair(possible_hand2)}.')
            break
        elif pair(possible_hand1) != None:
            print(f'Player 1 wins with {pair(possible_hand1)}.')
            break
        elif pair(possible_hand2) != None:
            print(f'Player 2 wins with {pair(possible_hand2)}.')
            break




        else:
            stringy = str(possible_hand1)
            g = list(rank_dict(possible_hand1))
            g.sort()
            print(g)
            if g[len(g)-1] == 14:
                g[len(g)-1] = 'A'
            if g[len(g)-1] == 13:
                g[len(g)-1] = 'K'
            if g[len(g)-1] == 12 :
                g[len(g)-1] = 'Q'
            if g[len(g)-1] == 11 :
                g[len(g)-1] = 'J'

            if g[len(g)-1] == 10 :
                high = stringy[stringy.find(str(g[len(g)-1])):stringy.find(str(g[len(g)-1]))+4]


            else:
                high = stringy[stringy.find(str(g[len(g)-1])):stringy.find(str(g[len(g)-1]))+3]

            strangy = str(possible_hand2)
            z = list(rank_dict(possible_hand2))
            z.sort()
            print(z)
            if z[len(z)-1] == 14:
                z[len(z)-1] = 'A'
            if z[len(z)-1] == 13:
                z[len(z)-1] = 'K'
            if z[len(z)-1] == 12 :
                z[len(z)-1] = 'Q'
            if z[len(z)-1] == 11 :
                z[len(z)-1] = 'J'

            if z[len(z)-1] == 10 :
                higher = strangy[strangy.find(str(z[len(z)-1])):strangy.find(str(z[len(z)-1]))+4]


            else:
                higher = strangy[strangy.find(str(z[len(z)-1])):strangy.find(str(z[len(z)-1]))+3]


            print(z[len(z)-1])
            print(g[len(g)-1])
            print(f'The players tie on high cards of {high} for player 1 and {higher} for player 2 ')
            break
    looper = 1
    while looper = 1:
        keep_going = input('Would you like to continue?').upper()
            if keep_going == 'Y' :
                break

            if keep_going == 'N' :
                quit()

            else:
                print('Try again.\n')
                continue
    continue
