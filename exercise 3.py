number=10
print("Welcome to the game!")
print("You have 5 chances to guess the hidden number")
gc = 0
while gc < 5:
    gc = gc + 1
    guess = int(input("Enter the number- "))
    if guess < 10:
        print("You had entered the smaller number...try some larger number")
        print("Chances left- ", 5 - gc)
        continue
    elif guess > 10:
        print("You had entered the larger number...try some smaller number")
        print("Chances left- ", 5 - gc)
        continue
    else:
        print("Hurray!!! You guessed it correct.")
        exit()
print("Game Over!!! ")


