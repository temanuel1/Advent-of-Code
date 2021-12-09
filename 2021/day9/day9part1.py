f = open('2021/day9/test.txt', 'r')
content = f.read()
numList = content
lines = numList.split("\n")
numsInLine = len(lines[0])
print(numsInLine)
A = 1
riskLevel = 0
finalNumList = []
for line in lines:
    for i in range(0, len(line), A):
        # convert to int, after the slicing process
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
  
print(len(finalNumList))

for i in range(len(finalNumList)):
    if isUp(i):
        if i == 0:
            if topLeftLow(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
        elif i == (numsInLine - 1):
            if topRightLow(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
        else:
            if topDefaultLow(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
    elif isDown(i):
        if i % numsInLine == 0:
            if bottomLeftLow(i) :
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
        elif i == (len(finalNumList) - 1):
            if bottomRightLow(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
        else:
            if bottomDefaultLow(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
    else:
        if i % numsInLine == 0:
            if leftDefaultLow(i):              
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
        elif i % (numsInLine - 1) == 0:
            #print(i)
            if rightDefaultLow(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))
        else:
            if default(i):
                print("Low point at index: " + str(i))
                riskLevel += (1+int(finalNumList[i]))

#Should be 465
print("Answer: " + str(riskLevel))