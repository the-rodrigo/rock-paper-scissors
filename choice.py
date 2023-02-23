def choice(value, options=['scissors', 'paper', 'rock']):
    while True:
        if value in options:
            return value
        else:
            print('You choose an invalid option. Your options are rock, paper or scissors.')
            value = input('Which option do you choose?\n').lower()
