def winner(your_choice, cpu_choice):
    if your_choice == cpu_choice:
        print('It is a draw.')
        result = 0
    elif your_choice == "scissors":
        if cpu_choice == "paper":
            print('YOU WON')
            result = 1
        else:
            print('CPU WON')
            result = 1
    elif your_choice == "paper":
        if cpu_choice == "scissors":
            print('CPU WON')
            result = 1
        else:
            print('YOU WON')
            result = 1
    elif cpu_choice == "paper":
        print('CPU WON')
        result = 1
    else:
        print('YOU WON')
        result = 1

    return result
