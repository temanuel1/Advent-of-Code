f = open('2020/day1/nums.txt', 'r')
content = f.read()
##print(content)

list = content.split("\n")

solved = False

for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if ((int(list[i]) + int(list[j]) + int(list[k])) == 2020) and not solved:
                print("Numbers are: " + str(list[i]) + " and " + str(list[j]) + " and " + str(list[k]))
                solved = True
                print(int(list[i]) * int(list[j]) * int(list[k]))