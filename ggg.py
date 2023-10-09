secret = '7'
def play(tries):
    if tries > 0:
        print("You have " + str(tries) + " tries left.")
        guess = int(input("Guess a number between 1 and 10: "))
        global secret
        compare = int(secret)
        if guess == compare:
            print("You win!")
        else:
            print("You lose!")
            play(tries - 1)
   
def game():
    print("Welcome to the guessing game!")
    print("Input no. tries. . .")
    tries = int(input())
    play(tries)

game()