f = open('day1/numbershit.txt', 'r')
content = f.read()
##print(content)

updatedList = content.split("\n")

##print(updatedList)

windowBigger = 0


for i in range(len(updatedList)-3):
  if (int(updatedList[i]) < int(updatedList[i+3])):
    windowBigger +=1

print (windowBigger)