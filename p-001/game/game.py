import random
import sys
while True:
    try:
        l = int(input('Level: '))
        if l > 0:
            num = random.randint(1, l)
            break
    except ValueError:
        print()

while True:
    try:
        g = int(input('Guess: '))
        if g > 0:
            if g == num:
                print('Just right!')
                sys.exit(0)
            elif g > num:
                print('Too large!')
            elif g < num:
                print('Too small!')
    except ValueError:
        print()


