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

while player1 != [] or player2 != []:
    card1 = []
    card2 = []
    card1.append(player1[0])
    card2.append(player2[0])
    player1.pop(0)
    player2.pop(0)
    if card1[0].get('Power') > card2[0].get('Power'):
        player1.append(card1[0])
        player1.append(card2[0])
        print(f'player1 card {card1[0]} beats player2 card {card2[0]}')
    elif card1[0].get('Power') < card2[0].get('Power'):
        player2.append(card1[0])
        player2.append(card2[0])
        print(f'player2 card {card2[0]} beats player1 card {card1[0]}')
    else:
        player1.append(card1[0])
        player2.append(card2[0])
        print(f'player2 card {card2[0]} is equal to player1 card {card1[0]}')

if player1 == []:
    print('Player 2 Wins!')
else:
    print('Player 1 Wins!')
