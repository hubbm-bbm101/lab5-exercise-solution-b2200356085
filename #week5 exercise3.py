#week5 exercise3
import random
game = random.randint(1, 100)
while True:
    guess = int(input("please write a number between 1 and 100:  "))
    if guess == game:
        print("you win!!")
        break
    if guess < game:
        print("decrease the number")
    if guess > game:
        print("increase the number")