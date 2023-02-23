import random

from choice import choice as ch
from start import start as st
from winner import winner as wn

result, options, your_choice = st()

while True:
    if result == 1:
        break
    else:
        cpu_choice = random.choice(options)

        print('Your options are rock, paper or scissors.')
        your_choice = input('Which option do you choose?\n').lower()

        your_choice = ch(your_choice)

        print(f'You chose {your_choice} and CPU chose {cpu_choice}.')

        result = wn(your_choice, cpu_choice)
