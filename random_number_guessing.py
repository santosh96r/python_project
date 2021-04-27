# random number guessing game

import random

flag = True
while flag:
    num = input('Enter a number for an upper bound: ')

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False

    else:
        print("Invalid input!. Try Again!")
        
secret = random.randint(1, num)

guess = None
no_of_guess = 1


while (no_of_guess <= 6):
    guess = input('Please type a number between 1 and ' + str(num) + ":")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('you got it!')
        print('It took you ', no_of_guess , 'guesses!')
    else:
        print('Please try again!')
    no_of_guess += 1      


if  (no_of_guess >6):
    
    print("Game Over !")

         



        
        

        
