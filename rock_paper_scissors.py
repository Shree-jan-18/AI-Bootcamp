import random

map_short = {'r':'rock','p':'paper','s':'scissors'}
rules = {('rock','scissors'),('scissors','paper'),('paper','rock')}

while True:
    p = input('r/p/s: ').strip().lower()
    if p not in map_short:
        print('invalid'); continue
    player = map_short[p]
    comp = random.choice(list(map_short.values()))
    print('Computer chose', comp)
    if player == comp:
        print('Tie')
    elif (player,comp) in rules:
        print('You win')
    else:
        print('Computer wins')
    if input('again? y/n: ').strip().lower() != 'y': break
