secret_number = 3
i = 0
while i < 3:
    ans = int(input('Guess: '))
    i += 1
    if ans == 3:
        print('You Won! ')
        exit()