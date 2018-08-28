name = input("You arrive at the gates of a giant medieval castle. A butler opens the door. He greets you and says, "
             "'Welcome to His Highness Castle! What is your name?'"
             "\n Type your name here:  ")
print (name)

job = input("'And What is your business here, " + name +"? Your occupation?' (You can say: Knight, gardener, the King, or maid.) ")
print (job)

if (job == "Knight" or job == "knight" or job == "a knight"):
    print("\n'Oh. Excuse me for not realizing this sooner! I should have guessed by the steel armor and lance. "
          "\nWelcome to the castle! Please make yourself at home here! The King has been waiting for you.'")

elif (job == "gardener" or job == "Gardener" or job == "a gardener"):
    print("\n'Oh, you! Where have you been!? The Queen has been expecting you for days! "
          "\nThere's a strange plant destroying all the life in the garden! "
          "It's so beast-like, and it's been causing her majesty so much distress! "
          "\nHow could you make her wait so long?! You'd better get to it right away!'")

elif (job == "king" or job == "King" or job == "the king"):
    print("\n'How dare you show up and mock his highness like this! Leave now you wretched liar or "
          "I'll have to get Mrs. Peterson to kick you out with her broomstick!'")
    a1 = input("Press 'a' to leave now or press 'b' to run past the butler into the castle.")
    if a1 == "a":
        print()
    elif a1 == "b":
        print()

else:
    print("\n'Ah, a new member of the castle staff! You've come at the right time! There's a lot of work that needs to be done today. "
          "The chores for today are: ")
    chores = [" washing the windows", " sweeping the Grand Hallway", " cleaning the privy", " serving the King lunch at noon"]
    def what_chores(chores):
        times = 1
        for chore in chores:
            if times == len(chores):
                print (" and" + chore + ".'")
                times = 1
            elif times < len(chores):
                print(chore + ",")
                times +=1
    what_chores(chores)
    chore_doing = 0
    chores_done = 0
    while chores_done == 0:
        while chore_doing == 0:
            chore_doing = input(
                "Which chore would you like to do first? Type 'a' for washing the windows, 'b' for sweeping the Grand Hallway,"
                "\n'c' for cleaning the privy, or 'd' for serving the king lunch at noon. ")
        if chore_doing == "a":
            print("\nYou choose to wash the windows first.")
            chores_done = 1
        elif chore_doing == "b":
            print("\nYou choose to sweep the Grand Hallway first.")
            chores_done = 1
        elif chore_doing == "c":
            print("\nYou choose to clean the privy first.")
            chores_done = 1
        else:
            print("\nYou can't do that right now.")
            chore_doing = 0






