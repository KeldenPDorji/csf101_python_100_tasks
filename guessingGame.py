
print('Input number of tries:')
tries = int(input())

print('Guess a number:')
secret = '8'
guess = input()

if guess == secret:
    print((guess == secret))
    print('MATCHED')
else:
    print('FALSE')
    tries = tries -1
    if tries > 0:
        print('Guess a number:')
        guess = input()
        if guess == secret:
            print((guess == secret))
            print('MATCHED')
        else:
            print('FALSE')
            tries = tries -1
            if tries > 0:
                print('Guess a number:')
                guess = input()
            else:
                print('NO MORE TRIES')
    else:
        print('NO MORE TRIES')


