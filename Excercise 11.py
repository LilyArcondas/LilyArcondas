#EXERCISE 11: Let’s build a student grading system - if, for loops, random, input method, lists
#Write a program that takes a list of classes like so: ["Math", "English", "Science"] and that prompts students for their first
# and last name. The program should loop over all the classes in the list and assign a random number to a variables called gpa.

#Import random numbers
#Create a list of classes
#Prompt users to get first and last name
#Loop over all the classes in the list
#Assign random numbers to a variable gpa
#If the gpa is less than or equal to 2.5, print “You failed this class”
#Else if the gpa is greater than or equal to 2.6 and less than or equal to 3.0 then print “You get a B”
#Else if the gpa is greater than 3.0 print “You get an A”
#For each class print: print("First name is ", firstname, "and last name is ", lastname, "with class ", var, "and gpa ", gpa)

import random

classes = ["Science", "History", "English", "Math"]

firstname = input("What is your first name? ")
lastname  = input ("What is your last name? ")

print("\n")

for x in classes:
    print (x)
    gpa = float(random.randint(0,5))
    print (gpa)
    if gpa <= 2.5:
        print("You failed this class.")
    elif (gpa >= 2.6 and gpa <= 3.0):
        print("You get a B")
    elif gpa > 3.0:
        print("You get an A")
    print ("First name is ", firstname, " and last name is ", lastname, " with class ", x, " and gpa ", gpa, ".\n")