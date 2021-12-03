f = open('day3/file.txt', 'r')
content = f.read()
binList = content.split('\n')
binList2 = content.split('\n')

c = 0
zeroes = 0
ones = 0

def binaryToDecimal(n):
    return int(n,2)

def oxygenGen(moreOnes, c):
    if(moreOnes):
        return list(filter(lambda binary: binary[c] == '1', binList))
    else:
        return list(filter(lambda binary: binary[c] == '0', binList))

def co2Scrub(moreOnes, c):
    if(moreOnes):
        return list(filter(lambda binary: binary[c] == '0', binList2))
    else:
        return list(filter(lambda binary: binary[c] == '1', binList2))

while c < 12:
    for binary in binList:
        if (binary[c]) == "0":
            zeroes+=1
        else:
            ones+=1
    moreOnes = ones>=zeroes
    binList = oxygenGen(moreOnes, c)
    zeroes-=zeroes
    ones-=ones
    #print(c)
    c+=1

c=0
while c < 12 and len(binList2) > 1:
    for binary in binList2:
        if (binary[c]) == "0":
            zeroes+=1
        else:
            ones+=1
    moreOnes = ones>=zeroes
    binList2 = co2Scrub(moreOnes, c)
    zeroes-=zeroes
    ones-=ones
    c+=1


print ("The life support rating is: " + str(binaryToDecimal(binList[0]) * binaryToDecimal(binList2[0])))