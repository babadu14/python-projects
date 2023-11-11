import random
number = random.randint(1,100)
guess = 0
while True:
    guess = int(input("ENTER A NUMBER -> "))
    if guess < number:
        print("GUESS HIGHER")
    elif guess > number:
        print("GUESS LOWER")
    else:
        print("YOU WON")
        break