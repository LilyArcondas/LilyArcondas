x = 10
y= 5
if x>y:
    print ("x is greater than y.")


name = input("What is your name? ")
print ("Hello " + name + (", welcome to the Racine Creative Center!"))
like_to_do = input("What would you like to learn about here? Drawing, coding, or filming? ")
if like_to_do == "drawing":
    print("We have big drawing tablets here and programs like photoshop and illustrator that you can learn to draw with.")
    like_to_do = input("Is there anything else you would like to learn about here? Coding or filming? ")
elif like_to_do == "coding":
    print("We currently have a coding class for girls that goes from 1pm to 3pm. You're welcome to join us if you want!")
elif like_to_do == "filming":
    print("We have professional cameras, a greenscreen, and a microphone to help you learn how to make professional videos here. We alse have programs like Adobe Premiere and After Effects, so that you can learn how to edit your videos after you film them. We also have a small class on making films, so if you are interested you are always allowed to come on in and check it out!")

