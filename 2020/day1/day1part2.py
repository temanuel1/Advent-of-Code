f = open('2020/day1/input.txt', 'r')
content = f.read()
##print(content)

numList = content.split("\n")

for num in numList:
    for i in range(len(numList)-2):
        if ((int(num) + int(numList[i]) + int(numList[i+1])) == 2020):
            print(num, numList[i], numList[i+1])
            print(int(num) * int(numList[i]) * int(numList[i+1]))