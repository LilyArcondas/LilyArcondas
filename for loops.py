infinity = ["You are trapped in a loop", "You are trapped in a loop"]

how_i_feel = input("Are you feeling naughty or nice today? ")

def loop(infinity):
    for line in infinity:
        print (line)
        infinity.append("You are trapped in a loop")

if how_i_feel == "naughty":
    loop(infinity)
else:
    print("Then you will not be trapped in a loop :)")

