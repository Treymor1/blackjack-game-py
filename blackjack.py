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
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cards = []
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

shuffle()
cards_dealt = deal(2)
print(cards_dealt)




