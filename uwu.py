start = "Dora needs your help to get to a surprise party at the barn! You will need to travel throughout the land to get there."
gameplaying = "yes"
print(start)

while gameplaying == "yes":
    userChoice = input("you are in the forest and you have encountered Isa the Iguana. She is lost and asks you which path she should travel on. Press 1 for the left path and press 2 for the right path. ")

    if userChoice == "1":
        print("You picked the wrong path and fell into a pit of snakes. ")
        gameplaying = input("would you like to try again? type yes or no ")
    elif userChoice == "2":
        print("you picked the correct path and are out of the forest! congratulations! ")
        print("")
        gameplaying = "no"
    else:
        print("please pick one of the paths: 1 or 2. ")
        gameplaying = input("would you like to try again? type yes or no")
        if gameplaying == "no":
            quit()

gameplaying = "yes"

while gameplaying == "yes":
    userChoice = input("You keep walking and you find Tico the Squirrel, who cannot get to the party because his car broke down. You decide to help him and give him tools. do you give him a taco, a tire pump, or a hammer? ")

    if userChoice == "taco":
        userChoice = input("sorry that is wrong, try again ")
    elif userChoice == "tire pump":
        print("good job Tico fixed his car and was able to give you a ride to the party. you win ")
        print("")
        print("congratulations you made it to the party :) ")
        gameplaying = "no"
    elif userChoice == "hammer":
        userChoice = input("sorry that is wrong, try again ")

    else:
        print("please pick one of the tools ")
        gameplaying = input("please try again ")
        if gameplaying == "no":
            quit()

