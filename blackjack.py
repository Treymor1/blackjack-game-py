import random
def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for i in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

suits = ["spades","clubs","hearts","diamonds"]
ranks = [{"rank":"A","value":11},
         {"rank":"2","value":11},
         {"rank":"3","value":11},
         {"rank":"4","value":11},
         {"rank":"5","value":11},
         {"rank":"6","value":11},
         {"rank":"7","value":11},
         {"rank":"8","value":11},
         {"rank":"9","value":11},
         {"rank":"10","value":11},
         {"rank":"","value":11},
         {"rank":"A","value":11},
         {"rank":"A","value":11},]

cards = []
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

shuffle()
card = deal(1)[0]

rank_dict = {"rank":rank, "value":value}
print(rank,value)




