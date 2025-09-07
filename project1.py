name = input("Enter your name ")

name = name.strip()

print ("Hello " + name + " Welcome to the game")

should_we_play = input("Do you want to play").lower()

should_we_play = should_we_play.strip()

if should_we_play == "y" or should_we_play == "yes" :
    print("we are going to play")
    weapon = input("Choice of weapon (sword/axe/none)").lower()

    weapon = weapon.strip()

    if weapon == "sword" :
        print("Sword added to your backpack")

    elif weapon == "axe" :
        print("Axe added to backpack")

    elif weapon == "none":
        print("No wepon added to backpack")

    direction = input("Do you want to go left or right? (Left/Right)").lower()

    direction = direction.strip


    if direction == "left" and weapon == "axe":
        print("Lucky u, you were able to hang on")
        choice = input("Okay now you see a bridge do you want to cross it or swim under it (Cross it/ Swim)").lower()
    
    elif direction == "left" :
        print("Sorry you fell of")
        quit()

    elif direction == "right":
        print("Okay we are going right")
        choice = input("Okay now you see a bridge do you want to cross it or swim under it (Cross it/ Swim)").lower()

        if choice == "swim" and weapon == "sword":

            choice=choice.stip()

            print("Lucky you, You killed the shark")
            next1 = input("Okay now do u want to go straight forward or  move toward the left (Straight/left)").lower()

            
        elif choice == "swim" :
            print("Sorry, You got eaten by a shark, Want to try again")
        

        elif choice == "cross it" or "crossit" :
            print("Great choice u made it safely")
            next1 = input("Okay now do u want to go straight forward or  move toward the left (Straight/left)").lower()

            next1 = next1.strip()

            if next1 == "straight":
                print("Glad you could make it,  u beat the game this is the gold")
                quit()

            elif next1 == "left" and weapon == "none":
                print("U barely missed the boulder because you were not equipped with a weapon u were light enough to dodge the huge boulder")
                print("U beat the game this is the gold, Bye")
                quit()

            elif next1 == "left" :
                print("U were so close such a wrong turn, You lose, Try again")

            else :
                print("Wrong answer")


    else:
        print("Sorry not a valid answer, you die")
else:
    print("Goodbye")
    quit()