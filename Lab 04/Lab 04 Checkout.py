import random
import sys
while True :
    print('\n\n\n\n\n\nYou have 7 guesses on what the Number is from a range of 1~50. You will be told Higher or Lower if incorrect.')
    Resistance = random.randint(0,50)
    print(Resistance)
    count = 1
    gameover = False
    valid = True
    while True:
        if count > 7 :
            gameover = True
            break
        print('\nPlese input your Guess. Guess Number:', count)
        guess = input('> ')
        count += 1
        Valid = True
        try:
            guess = int(guess)
        except ValueError:
            print("This input is not a number. You have been Penaltized and lost a Guess count.")
            Valid = False
        if Valid :
            if guess > 50 or guess < 0:
                print('This is an Invalid Guess. You have been Penaltized and lost a Guess count.')
            elif guess > Resistance :
                print('Too High')
            elif guess < Resistance :
                print('Too Low')
            elif guess == Resistance :
                print('Correct')
                break

    if gameover :
        print('You have Lost. Would you like to Try again? ( Y / N )')
    else :
        print('You have guessed the correct number. Would you like to try again? ( Y / N )')
    while True :
        retry = input ('> ').lower()
        if retry not in ['y','n'] :
            print("That was not a valid answer. Plese type 'Y' for yes and 'N' for No")
            print('Would you like to Try again?')
        elif retry == 'y' :
            break
        else :
            sys.exit()
