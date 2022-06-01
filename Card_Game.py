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
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    stack = []
    
    if card1['Power'] == card2['Power']:
        while card1['Power'] == card2['Power']:
            print(f"WAR P1-{card1['Power']} P2-{card2['Power']}")
            stack.append(card1)
            stack.append(card2)
            if len(player1) < 2:
                player2.extend(stack)
                player2.extend(player1)
                player1 = []
                print(f"PLAYER-1 {card1['Power']}\t{card2['Power']}\tP1 {len(player1)} P2 {len(player2)}")
                break
            elif len(player2) < 2:
                player1.extend(stack)
                player1.extend(player2)
                player2 = []
                print(f"PLAYER-2 {card1['Power']}\t{card2['Power']}\tP1 {len(player1)} P2 {len(player2)}")
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1['Power'] > card2['Power']:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print(f"PLAYER-1 {card1['Power']}\t{card2['Power']}\tP1 {len(player1)} P2 {len(player2)}")
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print(f"PLAYER-2 {card1['Power']}\t{card2['Power']}\tP1 {len(player1)} P2 {len(player2)}")

                
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print(f"PLAYER-1 {card1['Power']}\t{card2['Power']}\tP1 {len(player1)} P2 {len(player2)}")
    else:
        player2.append(card1)
        player2.append(card2)
        print(f"PLAYER-2 {card1['Power']}\t{card2['Power']}\tP1 {len(player1)} P2 {len(player2)}")

if len(player1) > 0:
    print('Player 1 Wins!')
else:
    print('Player 2 Wins!')
