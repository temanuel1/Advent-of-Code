f = open('2021/day6/nums.txt', 'r')
content = f.read()
##print(content)

updatedList = content.split(",")
integer_map = map(int, updatedList)
intList = list(integer_map)


c = 0

while c < 256:
    for num in range(len(intList)):
        if intList[num] == 0:
            intList.append(8)
            intList[num] = 6
        else:
            intList[num] -= 1
    print(c)
    c += 1

print(len(intList))
