f = open('2021/day8/input.txt', 'r')
content = f.read()
##print(content)

updatedList = content.split("\n")

uniqueOutput = 0

for entry in updatedList:
    entry = entry.split(" ")
    output = entry[11] + " " + entry[12] + " " + entry[13] + " " + entry[14]
    output = output.split(" ")
    for thing in output:
        if len(thing) == 2:
            #print(thing + " is unique")
            uniqueOutput+=1
        elif len(thing) == 3:
            #print(thing + " is unique")
            uniqueOutput+=1
        elif len(thing) == 4:
            #print(thing + " is unique")
            uniqueOutput+=1
        elif len(thing) == 7:
            #print(thing + " is unique")
            uniqueOutput+=1

print("Answer is: " + str(uniqueOutput))



