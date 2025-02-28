import random
import time

#02/18/25 lesson
#ask user what year they are born in, then print out hold old they will be in 2025

yearborn = input("What year were you born in?\n")
yearborn = int(yearborn)
print("You will be "+ str(2025-yearborn) + " in 2025")

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

#02/24/25 lesson
#program that asks the user what item they want to remove from the list and removes that item from the list. 
#keep asking the user what item they want to remove until they respond "stop".

groceries = ["cheeze its","nerd gummy clusters","doritos","pepsi","mountain dew","cocoa puffs"]

def remove_items():
    while True:
        print("You have: "+ ", ".join(groceries)+ " in your grocery list")
        item = input("What item do you want to take out?\n")
        
        groceries.remove(item)
        
        keep_going = input("Do you want to take anything else out? (say stop to stop)\n")

        if keep_going == "stop":
            break
        else:
            print("ok")

remove_items()

#02/26/2025 lesson
#make roulette wheel, dont let user bet over the amount of money they have

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    money = 1000
    spaces = generate_wheel()

    while True:
        print("You have $"+ str(money))
        
        bet = input("How much money do you want to bet?\n")
        bet = int(bet)

        if bet<= money:
            already_sold=False

            color = input("What color do you want to bet on?\n")

            print("The wheel beings to spin...")
            time.sleep(2)
            landed = spin_wheel(spaces)
            print("The ball has landed on " + landed +"...")
            if color==landed:
                win = 2*bet
                money = (money-bet)+win
                print("You won $"+ str(win)+"!")
            else:
                print("Womp womp, you lost $"+ str(bet))
                money = money-bet

            if money==0:
                # if already_sold==False:
                #     sell_car=input("Do you want to sell your car?\n")
                #     if sell_car == "yes":
                #         already_sold = True
                #         print("Let me asses the value of your car...")
                #         time.sleep(2)
                #         value = random.randint(400,5000)
                #         print("You now have $"+ str(value) + " more dollars to gamble with!")
                #         money = money + value
                # else:
                print("You're broke... go away")
                break
            else:
                print("You now have $"+ str(money))

            play_again = input("Do you want to play again?\n")

            if play_again == "no":
                break
            else:
                print("Im gonna take that as a yes")
        else:
            print("Dont get too ahead of yourself buddy, thats more money than you have")

play_game()

#Forgot which day this lesson was
#create function with two parameters: item and price, and update the menu dictionary

menu = {"Pizza":1.99,"Soda":0.69,"Double Chunck Chocolate Chip Cookie":2.49}

def add_item(item,price):
    menu[item]=price
    return menu

add_item("Chicken bake",2.49)
print(menu)