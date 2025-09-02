name = input("Enter your name")
print ("Hello" + name + "Welcome to the game")

should_we_play = input("Do you want to play").lower()

if should_we_play == "yes" :
    print("we are going to play")

elif should_we_play == "YES" :
    print("WE ARE GOING TO PLAY")

else:
    print("Goodbye")