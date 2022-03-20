import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace',  'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10',   'Power': 10},
    {'Figure': '9',    'Power': 9}
    ]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
    

random.shuffle(allCards)

player1 = []
player2 = []
player1 += allCards[:12]
player2 += allCards[12:24]

print(player1)
print('\n')
print(player2)

card1 = []
card2 = []
while player1 != [] or player2 != []:
    card1 += dict(player1[0])
    card2 += dict(player2[0])
print("\n")
print(card1, card2)
