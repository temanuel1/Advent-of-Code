f = open('2020/day1/input.txt', 'r')
content = f.read()
##print(content)

numList = content.split("\n")

for num in numList:
    for i in range(len(numList)-1):
        if (int(num) + int(numList[i])) == 2020:
            print(int(num) * int(numList[i]))