import random

x = random.randint(1,10)
print('Guess a number between 1 and 10')
y = input()
if (x == y):
    print('You win! The number was', x)
else:
    print('Oops! The number was', x)
y = input()
