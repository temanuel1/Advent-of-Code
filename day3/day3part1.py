f = open('day3/file.txt', 'r')
content = f.read()

updatedList = content.split('\n')

def binaryToDecimal(n):
    return int(n,2)

zeroes = 0
ones = 0
gammaRate = ""
epsilonRate = ""

for i in range(len(updatedList[0])):
    for j in range(len(updatedList)):
        bits = updatedList[j]
        if int(bits[i]) == 0:        
            zeroes +=1
        else:
            ones +=1
    #print (zeroes, ones)
    if zeroes > ones:
        gammaRate += "0"
        epsilonRate += "1"
    else:
        gammaRate += "1"
        epsilonRate += "0"
    zeroes -= zeroes
    ones -= ones

##print (gammaRate, epsilonRate)


print (binaryToDecimal(gammaRate) * binaryToDecimal(epsilonRate))