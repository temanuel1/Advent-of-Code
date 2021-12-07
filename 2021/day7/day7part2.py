f = open('2021/day7/input.txt', 'r')
content = f.read()
##print(content)

totalFuel = 0
result = 1000000000

numList = content.split(",")
integer_map = map(int, numList)
intList = list(integer_map)
intList.sort(reverse=True)
#print(intList)

for i in range((intList[0])+1):
    #print("i: " + str(i))
    for num in intList:
        #print("Fuel used " + str(num - i))
        difference = abs(num - i)
        totalFuel+= ((difference) * (difference + 1)) / 2
    #print("Test " + str(i+1) + ": Total Fuel = " + str(totalFuel))
    #print(i, totalFuel)
    if (totalFuel < result):
        #Last one printed is the answer
        result = int(totalFuel)
    totalFuel = 0


print("Answer is: " + str(result))