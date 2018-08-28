idea = "bad"
if idea == "good":
    print("A great intro")


name = input("Welcome to Felinia, a magical land inhabited by cats! What is your name? ")
print ("Greetings, " + name + "! You are the hero of this adventure!")



if idea == "bad":
    print ("\nFelinia needs you help! The evil Doctor Nyan has taken almost all of the yarn in Felinia to himself! \nYarn keeps getting more and more scarce, the kittens are fighting over what little yarn is left! \nYour quest is to find Doctor Nyan and bring the stolen yarn back to the kittens of Felinia! Good Luck!")
    area=input("\nYou set off to go find Doctor Nyan. You are in an open field. You can see a forest, and a cat village in the distance. \nWhere do you want to go? Type 'a' to go to the forest, or type 'b' to go to the cat village. ")
    if area == 'a':
        print("\nYou decide to venture into the forest.")
        print("You get to the forest and find a thread of string on the ground. You put it in your bag.")
    elif area =='b':
        print("\nYou decide to visit the nearby village for clues.")