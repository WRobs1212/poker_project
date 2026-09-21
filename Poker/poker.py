#I'm going to get this out of the way now: most of my single-letter variables (g,j,x,y,z) function as iterables, so i felt no incentive to create funky names for them
#similarly, many of the lists I create get repurposed so they are also often called empty_list
import cards

deck = cards.Deck()
deck.shuffle()

#import cards and shuffles deck for further use

workable_deck = (str(deck))
workable_deck = workable_deck.split(',')
#as you may imagine, workable_deck make the deck of cards usable for the rest of the program

#this begins the overarching loop until the deck has <9 cards
while len(workable_deck) >= 9 :
    hand1_list = []
    hand2_list = []
    foundation_list = []
    for i in range(2):
        #importantly, each time a card is added to a hand, it is removed from the deck
        hand1_list.append(workable_deck.pop())
        hand2_list.append(workable_deck.pop())

    for i in range(5) :
        foundation_list.append(workable_deck.pop())
    #these each create the different parts of our poker game and iterate over the workable_deck to craft each hand



    print("player 1's hand is" , hand1_list , "\n")
    print("player 2's hand is" , hand2_list , "\n")
    print("the foundation is" , foundation_list , "\n")

#prints the hands of each player and the foundation

    possible_hand1 = hand1_list + foundation_list
    possible_hand2 = hand2_list + foundation_list

#these allow us to check the hand and foundation for each possibel card combination


#organizes cards in a dictionary by rank
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
            #I chose to convert these to number so comparisons later on will be easier
            else:
                rank = int(rank)

            #adds the suit(s) of each rank as values to the rank key
            suit = list(str((hand)[x]).split('-')[1])


            if rank in rdict:
                rdict[rank] = rdict[rank] + suit
            else:
                rdict[rank] = suit

        return rdict


#organizes cards into a dictionary based on suit
    def suit_dict(hand) :
        sdict = {}
        for x in range(7) :
            prank = str((hand)[x]).split('-')[0]
            rank = [prank]

            suit = str((hand)[x]).split('-')[1]

#adds the rank(s) of each suit as values to the suit key
            if suit in sdict:
                sdict[suit] = sdict[suit] + rank
            else:
                sdict[suit] = rank

        return sdict







#Each function accepts hand as an argument so that possible_hand1 and possible_hand2 can be checked independently
    def straight_flush(hand) :
        empty_list = []
        #I'll explaine the hearts reaction, but all the others operate the same, so it should be fine
        #First, we check to see if hearts are even in the hand
        if 'H' in suit_dict(hand) :
            #Then we see if there are 5 (since you need 5 to have a flush). If not, we'll check the other suits
            if len(suit_dict(hand)['H']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'H' in hand[j] :
                    #we iterate through our hand, and add each heart to a new list
                     empty_list.append(hand[j])
                     j += 1
                    else:
                        #if the card isn't an h, move on to the next
                        j += 1
                        continue

#now that we have the hearts added to a list, we just need to see if they're a straight
                z = 0
                value_list = []
                while z < len(empty_list):
                    #This is to convert and add any strange ranks to a new list so they're easier to mess with
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
                #Sort the value list low to high
                #Honestly this would be better if I used my straight definition because I rewrote it and I'm quite proud of it
                #This is the first function I wrote, though, and I dont want to mess it up and be forced to stay up super late
                while len(value_list) > 5:
                    #Essentially this compares some of the middle values to the end values and removes enf values if they're off
                    if value_list[0] + 3 != value_list[3]  and value_list[0] + 2 != value_list[2]:
                        value_list.pop(0)
                        continue
                    if value_list[len(value_list)-1] - 2 != value_list[len(value_list) - 3] and value_list[len(value_list)-2] - 2 != value_list[len(value_list) - 4]:
                        value_list.pop()
                        continue

#This checks the straight leftover
                if value_list[0] + 1 == value_list[1] and value_list[1] + 1 == value_list[2] and value_list[2] + 1 == value_list[3] and value_list[3] + 1 == value_list[4]:


                    winning_hand = []
                    x = 0
                    #Converts back to proper rank
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
#returns straight flush
                    return f'{winning_hand}, which is a straight flush.'
        #As I said, literally the same as hearts (It would've been a good idea to create a function for this)
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
        #Same as hearts and spades
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
#Same as the rest
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




#Four of a kind was easy and I kind of cheated. Essentially if I know that there are four of a rank in a hand, I know there must be one of each suit, so I just added each suit to the rank.
    def four_kind(hand) :
        x = 0
        #Common theme where I iterate through a list
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
                    #converts these bad boys back to their real forms
                winning_hand = f'{g}-H, {g}-D, {g}-S, {g}-C, which is a four-of-a-kind'
                x += 1
                return winning_hand
            else:
                x += 1


#Full house probably took me the longest (hard to believe considering the abomination that is striaght flush)
    def full_house(hand) :
        x = 0
        list_format = list(rank_dict(hand))
#I create a list of the values and iterate through the liste (remember, common theme)
        while x < len(list_format):
            g = list_format[x-1]
            #First, I find the three of a kind
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

#This is kind of like a duct tape for me. I got an error one time and this seemed to fix it.
                if g not in list_format:
                    return None
                list_format.remove(g)


                j = 0
                #Next, I find the pair
                while j < len(list_format):
                    z = list_format[j-1]
                    if len(rank_dict(hand)[z]) >= 2:
                        suit = rank_dict(hand).pop(z)
                        while len(suit) > 2 :
                            suit.pop()



                        break



                    else:
                        j += 1
                        continue


#This is kind of like a duct tape for me. I got an error one time and this seemed to fix it.
                if len(rank_dict(hand)[z]) < 2:
                    return None
                if z == 14:
                    z = 'A'
                if z == 13:
                    z = 'K'
                if z == 12 :
                    z = 'Q'
                if z == 11 :
                    z = 'J'

#Put them together
                winning_hand = f'{g}-{suit1[0]}, {g}-{suit1[1]}, {g}-{suit1[2]}, {z}-{suit[0]}, {z}-{suit[1]}, which is a full house.'
                return winning_hand


            else:
                x += 1
                continue


#My flush is pretty much the first part of my straight flush (and by pretty much I mean copied and pasted)
    def flush(hand) :
        #we create an empty list
        empty_list = []
        if 'H' in suit_dict(hand) :
            #we check if there are hearts or spades or diamonds or clubs, then we check if there are five or more of them
            if len(suit_dict(hand)['H']) >= 5 :
                j = 0
                while j < len(hand):
                    if 'H' in hand[j] :
                        #if there are, we iterate through the hand, adding each card that has a heart
                        empty_list.append(hand[j])
                        j += 1
                    else:
                        j += 1
                        continue
#wokrs the same
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


#works the same
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


#works the same
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

#if, in fact, there are not five of any suit, it returns None
        if empty_list == []:
            return None
            #otherwise it'll return the list we made that contains our flush
        return f'{empty_list}, which is a flush'







#As I said above, this straight definition makes me feel like an actual computer scientist (even if it is very base level)
    def straight(hand):
        #first, we need a sorted list of the ranks in the hand
        y = list(rank_dict(hand))
        y.sort()
        #Next we'll check if there are 7 unique ranks, if so, this is where it gets cool.
        if len(y) == 7:
            #Essentially, with seven ranks, our list must look like this:
            #[1,2,3,4,5,6,7]
            #You may notice that no matter what, 3,4,5 must be part of the straight_flush
            #because of this, if I notice that the final position is not position3 + 4, I know I can remove it because it isn't part of the straight
            if y[2] + 4 != y[6] :
                y.remove(y[6])
            #By this same principle, I can look at position4 and if the beginning position is not postioin4 - 4, I can remove it
            if y[4] -4 != y[0] :
                y.remove(y[0])
            #I then do essentially the same thing again but with 6 cards, making my list smaller and only exclusive of 1 card
            #[1,2,3,4,5,6]
            #Now 2,3,4,5 are part of the straight no matter what, so I just check the ends again
        if len(y) == 6:
            if y[1] + 4 != y[5]:
                y.remove(y[5])
            if y[4] - 4 != y[0] :
                y.remove(y[0])
        #With less than 5 ranks, there is no possibilty of a straight
        if len(y) < 5:
            return None
            #You need at least 5 cards to make a straight
            #Just in case I have 6 or 7 cards in a row, I arbitrarily remove the first card so it is the highest possible straight
        if len(y) > 5:
            y.remove(y[0])
            #checks for 7 card straight and reduces its length to 6 cards if it exists
            if len(y) > 5:
                y.remove(y[0])
                #checks for 6 card straight and reduces its length to 5 cards if it exists



#Last check (I bet it looks familiar to the striaght flush function) to see if each card is indeed one more than the previous
        if len(y) == 5 and y[0] + 1 == y[1] and y[1] + 1 == y[2] and y[2] + 1 == y[3] and y[3] + 1 == y[4]:
            x = 0
            empty_list = []
            stringy = str(hand)
            while x <= 4:
                #Have to change all the values back to their actual ranks
                #The way I choose to do this is my one regret with this function.
                #Using .find() to search for each one and then adding 3 was kind of annoying and it took me so long to actually get the parentheses and brackets right
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


#Yet after all that, we end with an easy return
            return f'{empty_list}, which is a straight'




#If my condiitons aren't met, nothing is returned
        else:
            return None






#Originally, I thought that I would be able to base this off my four of a kind function. Unfiortunately, as you may remember, I cheated just a little bit, whihc doesnt work for this one.
#Instead, I figured I had a perfectly good Full house function, whihc is a three of a kind and a pair, so I just used the first half of that\
#It is pretty much the exact same
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


#I did two pair similarly to full house as well. Copy and paste and then make some minor tweaks to how many cards I want of each and blah blah blah.
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


                if g not in list_format:
                    return None
                list_format.remove(g)



                j = 0
                while j < len(list_format):
                    z = list_format[j-1]
                    if len(rank_dict(hand)[z]) >= 2:
                        suit = rank_dict(hand).pop(z)
                        while len(suit) > 2 :
                            suit.pop()




                        break


                    else:
                        j += 1
                        continue



                if len(rank_dict(hand)[z]) < 2:
                    return None
                if z == 14:
                    z = 'A'
                if z == 13:
                    z = 'K'
                if z == 12 :
                    z = 'Q'
                if z == 11 :
                    z = 'J'


                winning_hand = f'{g}-{suit1[0]}, {g}-{suit1[1]}, {z}-{suit[0]}, {z}-{suit[1]}, which is a two pair'
                return winning_hand


            else:
                x += 1
                continue

#As you may know, a pair is half of a  two pair, so I only took half of two pair
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









#From here I iterate through each possibility (tie, p1 win, p2 win) and display which happened.
# Importantly, if one player wins a higher-value hand, the loop is broken and the second player's hand is not displayed.
#For example, if a player has a full house, their hand is only displayed as a full house and not a three of a kind or a two pair or a pair or a high card.
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


            print(f'The players tie on high cards of {high} for player 1 and {higher} for player 2 ')
            break
#Once we know who won the round, we need to know if you have any intention of continuing to play, so I just ask that and upper case the response so y and Y and n and N are the same.
    looper = 1
    while looper == 1:
        keep_going = input('Would you like to continue? y for yes, n for no.').upper()
        #if the answer is yes, I once break this loop and continue back up to the top.
        if keep_going == 'Y' :
            break
        #if the answer is no, I quit the program
        if keep_going == 'N' :
            quit()
        #if there way a misinput, I reprompt
        else:
            print('Try again.\n')
            continue
    continue
