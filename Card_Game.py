import random as rd

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
    

rd.shuffle(allCards)

player1 = []
player2 = []
player1 += allCards[:12]
player2 += allCards[12:24]

while len(player1) > 0 and len(player2) > 0:
    card1 = []
    card2 = []
    card1.append(player1[0])
    card2.append(player2[0])
    player1.pop(0)
    player2.pop(0)
    power1 = card1[0].get('Power')
    power2 = card2[0].get('Power')
    if power1 == power2:
        stack = []
        stack.append(card1[0])
        stack.append(card2[0])
        while len(player1) >= 2 and len(player2) >= 2:
            stack.append(player1[0])
            stack.append(player2[0])
            player1.pop(0)
            player2.pop(0)
            war1 = player1[0].get('Power')
            war2 = player2[0].get('Power')
            stack.append(player1[0])
            stack.append(player2[0])
            player1.pop(0)
            player2.pop(0)
            if war1 > war2:
                for i in stack:
                    player1.append(i)
                stack = []
                break
            elif war1 < war2:
                for i in stack:
                    player2.append(i)
                stack = []
                break
            else:
                continue
        else:
            break
                
    elif power1 > power2:
        player1.append(card1[0])
        player1.append(card2[0])
        print(f'PLAYER-1 {power1}\t{power2}\tP1 {len(player1)} P2 {len(player2)}')
    else:
        player2.append(card1[0])
        player2.append(card2[0])
        print(f'PLAYER-2 {power1}\t{power2}\tP1 {len(player1)} P2 {len(player2)}')

if len(player1) < len(player2):
    print('Player 2 Wins!')
else:
    print('Player 1 Wins!')
