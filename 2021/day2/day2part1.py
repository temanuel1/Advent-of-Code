f = open('day2/movements.txt', 'r')
content = f.read()

xPos = 0
yPos = 0

updatedList = content.split("\n")

for i in range(len(updatedList)):
    directions = updatedList[i]
    if (len(updatedList[i]) == 9):
        num = int(directions[8])
        xPos += num
    elif (len(updatedList[i]) == 6):
        num = int(directions[5])
        yPos += num
    else:
        num = int(directions[3])
        yPos -= num

print(xPos * yPos)