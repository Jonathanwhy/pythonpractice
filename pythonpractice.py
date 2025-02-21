import random

#02/18/25 lesson
#ask user what year they are born in, then print out hold old they will be in 2025

# yearborn = input("What year were you born in?\n")
# yearborn = int(yearborn)
# print("You will be "+ str(2025-yearborn) + " in 2025")

#02/21/25 lesson
#program that generates random number and has user guses what it is
#update the program to keep track of how many guesses the user made

random_num = random.randint(0,100)
guesses = 0

while True:
    guesses = guesses+1
    guess = int(input("guess a number 1-100\n"))
    if guess < random_num:
        print("the number you want is higher")
    elif guess > random_num:
        print("the number you want is lower")
    else:
        print("you guessed the number!!1!")
        print("It took you "+ str(guesses)+" guesses..")
        break
