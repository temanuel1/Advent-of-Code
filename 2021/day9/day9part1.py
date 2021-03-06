f = open('2021/day9/input.txt', 'r')
content = f.read()
numList = content
lines = numList.split("\n")
numsInLine = len(lines[0])
A = 1
riskLevel = 0
finalNumList = []
for line in lines:
    for i in range(0, len(line), A):
        finalNumList.append(int(line[i : i + A]))


def isUp(i):
    return i < numsInLine

def isDown(i):
    return i >= (len(finalNumList) - numsInLine)

def topLeftLow(i):
    return finalNumList[i] < finalNumList[i+1] and finalNumList[i] < finalNumList[i+numsInLine]

def topRightLow(i):
    return finalNumList[i] < finalNumList[i-1] and finalNumList[i] < finalNumList[i+numsInLine]

def topDefaultLow(i):
    return finalNumList[i] < finalNumList[i+1] and finalNumList[i] < finalNumList[i-1] and finalNumList[i] < finalNumList[i+numsInLine]

def bottomLeftLow(i):
    return finalNumList[i] < finalNumList[i+1] and finalNumList[i] < finalNumList[i-numsInLine]

def bottomRightLow(i):
    return finalNumList[i] < finalNumList[i-1] and finalNumList[i] < finalNumList[i-numsInLine]

def bottomDefaultLow(i):
    return finalNumList[i] < finalNumList[i+1] and finalNumList[i] < finalNumList[i-1] and finalNumList[i] < finalNumList[i-numsInLine]

def leftDefaultLow(i):
    return finalNumList[i] < finalNumList[i+1] and finalNumList[i] < finalNumList[i-numsInLine] and finalNumList[i] < finalNumList[i+numsInLine]
    
def rightDefaultLow(i):
    return finalNumList[i] < finalNumList[i-1] and finalNumList[i] < finalNumList[i+numsInLine] and finalNumList[i] < finalNumList[i-numsInLine]

def default(i):
    return finalNumList[i] < finalNumList[i+1] and finalNumList[i] < finalNumList[i-1] and finalNumList[i] < finalNumList[i-numsInLine] and finalNumList[i] < finalNumList[i+numsInLine]
  

for i in range(len(finalNumList)):
    if isUp(i):
        if i == 0:
            if topLeftLow(i):
                riskLevel += (1+int(finalNumList[i]))
        elif i == (numsInLine - 1):
            if topRightLow(i):
                riskLevel += (1+int(finalNumList[i]))
        else:
            if topDefaultLow(i):
                riskLevel += (1+int(finalNumList[i]))
    elif isDown(i):
        if i % numsInLine == 0:
            if bottomLeftLow(i) :
                riskLevel += (1+int(finalNumList[i]))
        elif i == (len(finalNumList) - 1):
            if bottomRightLow(i):
                riskLevel += (1+int(finalNumList[i]))
        else:
            if bottomDefaultLow(i):   
                riskLevel += (1+int(finalNumList[i]))
    else:
        if i % numsInLine == 0:
            if leftDefaultLow(i):              
                riskLevel += (1+int(finalNumList[i]))
        elif (i + 1) % numsInLine == 0:
            if rightDefaultLow(i):
                riskLevel += (1+int(finalNumList[i]))
        else:
            if default(i):
                riskLevel += (1+int(finalNumList[i]))

print("Part 1 Answer: " + str(riskLevel))