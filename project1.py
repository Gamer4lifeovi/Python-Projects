name = input("Enter your name")
print ("Hello" + name + "Welcome to the game")

should_we_play = input("Do you want to play").lower()

if should_we_play == "y" or should_we_play == "yes" :
    print("we are going to play")
    weapon = input("Choice of weapon (sword/axe)").lower()

    if weapon == "sword" :
        print("Sword added to your backpack")

    elif weapon == "axe" :
        print("Axe added to bapack")

    direction = input("Do you want to go left or right? (Left/Right)").lower()
    if direction == "left" :
        print("Okay you went left and fell of a bridge, game over,Try again")
        quit()
        

    elif direction == "right":
        print("Okay we are going right")
        choice = input("Okay now you see a bridge do you want to cross it or go under it")

        if choice == "swim" :
            print("You got eaten by a shark, you die,Try again")
            quit()
            

    else:
        print("Sorry not a valid answer, you die")
else:
    print("Goodbye")
    quit()