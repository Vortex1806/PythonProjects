import random

# numbers = [1,2,3,4,5,6]
# one = random.choice(numbers)
# two = random.choice(numbers)
# print(f'({one}, {two})')


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())