import random

def startup():
    print("Welcome to The Game of Googol")
    print("Inspired by Vsauce2")
    print("-----------------------------")
    print("1) Start Game")
    print("2) Exit")
    
    choose = int(input('>>'))
    try:
        if choose == 1:
            pass
        elif choose == 2:
            exit()
        else:
            startup()
    except ValueError:
        startup()
startup()

# Start
print("A googol is the large number 10^100. In decimal notation  it is written as the digit 1 followed by one hundred zeroes: 10 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000 ​000. ")
print("Your mission is to find the largest number in 50 papers.")
print("Rules:")
print("+ Find the largest number. It could be 1 to (a Googol).")
print("+ You must keep or pass the number. You cannot choose the number that you have passed.")
print("+ There will be 50 lines of numbers in total.")
input("You are ready? Press Enter to start!")

def keep():
    print("You have choose the number " + str(number))
    print(f"But there are still {turn_left} turn(s) left...")
    print("Let's check if that is the biggest number...")
    input("Press Enter... ")
    for keep_num in range(1, turn_left):
        keep_random_int = random.randint(1, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        if keep_random_int > number:
            print(f"You lose... The biggest number is {keep_random_int}")
            keep_turn_left = turn_left - keep_num
            print(f"And there are still {keep_turn_left} turn(s) left.")
            exit()
        else:
            pass
    print(f"You won! {number} was the biggest number!")
    input()
    exit()


for num in range(1, 51):
    #list_of_g = list(range(1, 100000000))
    number = random.randint(1, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    print("Number "+ str(num) + ":")
    print(number)
    print("1) Keep")
    print("2) Pass")
    cos = int(input())
    if cos == 1:
        turn_left = 50 - num
        keep()
        break
    elif cos == 2:
        pass


print("You lose... All of the numbers have been revealed!")
input()