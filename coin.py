import random
coin = ('head', 'tails')
head,tails = 0,0
games = 0
print('Hit x to exit')
while True:
    flip = random.choice(coin)
    your_choice = input('Type head or tails')
    if your_choice == 'x' or your_choice =='X':
        print("GAME OVER :(")
        print('Coin flippinf stats:')
        print('Games played = {}'.format(games))
        print('heads = {}'.format(heads))
        print('tails = {}'.format(tails))
        break
    if your_choice ==flip:
        print('coin landed on {}. Yeah boy you win!'.
              format(flip))
        games += 1
    else:
        print("Uh oh. Coin landed on {}. Better luck next"
              "time".format(flip))
        games +=1
    if flip == 'heads':
        heads += 1
    elif flip == 'tails':
        tails += 1
        
