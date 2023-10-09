def play(tries):
    print('tries called')
    print('troes: ', tries)
    tries = tries - 1
    if tries > 0:
        print('Guess a number:')
        guess = input()
        return str(guess)
    else:
        print('NO MORE TRIES')

def game():
    secret = '8' 
    guess = ''
    tries = ''
    print('Input number of tries:')
    tries = int(input())
    user_guess = play(tries)
    if user_guess == secret:
        print('MATCHED')
    else:
        play(tries)
        print('Tries not called')

game()



