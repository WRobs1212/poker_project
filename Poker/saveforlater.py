def straight_flush(hand) :
    if 'H' in suit_dict(hand) :
        if len(suit_dict(hand)['H']) >= 5 :
            for x in range(len(sorted(rank_dict(hand)))):

                if list(sorted(rank_dict(hand)))[x-1] + 1 == list(sorted(rank_dict(hand)))[x] :
                    print(list(sorted(rank_dict(hand)))[x])
            return hand
