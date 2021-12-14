f = open('day1/numbershit.txt', 'r')
content = f.read()
##print(content)

updatedList = content.split("\n")

##print(updatedList)

numBigger = 0


for i in range(len(updatedList)-1):
  if int(updatedList[i+1]) > (int(updatedList[i])):
    numBigger +=1

print (numBigger)