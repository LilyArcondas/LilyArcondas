#Write a program that loops through 3 times, prompts you for a string each time through the loop.
# Save the length of each string in a variable.
# If the length is less than 10 print “The length is short”,
# else the length is greater than 10 print “The length is long”

for x in range(0,3):
    string = input("Type a word to see if it is long or short: ").lower()
    how_long = len(string)
    if how_long < 10:
        if how_long == 1:
            print("Aww cute little baby word!")
        elif how_long == 0:
            print("What did your finger slip?")
        else:
            print("The length is short")
    elif string == "pnuemonoultramicroscopicsilicovolcanoconiosis":
        print("Do I even need to say it?")
    elif how_long > 10:
        print("The length is long")
    else:
        print("The length is not long or short")