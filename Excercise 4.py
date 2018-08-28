#Prompt the user to enter how many favorite colors they have.
# Use that variable in the range of the for loop to loop through and prompt the user agin for their favorite colors.
# Each time through the loop append that color to the list. Create another for loop and print out the colors.
# Output --> ["red", "purple", "green"]
number = int(input("How many favorite colors do you have? "))

colors = []
times = 0

for x in range(0, number):
    if times == 0:
        color = (input("Give one favorite color: "))
        print(color)
        colors.append(color)
        times += 1
    else:
        color = (input("Give another favorite color: "))
        print(color)
        colors.append(color)
        times += 1


print(colors)