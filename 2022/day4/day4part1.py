f = open('input.txt', 'r')
content = f.read()

sections = content.split('\n')
numContains = 0

for i in range(len(sections)):
    firstSection, secondSection = sections[i][:sections[i].index(",")], sections[i][sections[i].index(",") + 1:]
    firsts, seconds = firstSection.split('-'), secondSection.split('-')
    firstNums, secondNums = [], []
    for j in range(int(firsts[0]), int(firsts[1]) + 1):
        firstNums.append(j)
    for k in range(int(seconds[0]), int(seconds[1]) + 1):
        secondNums.append(k)
    if(len(firstNums) > len(secondNums)):
        if all(item in firstNums for item in secondNums):
            numContains+=1
    else:
        if all(item in secondNums for item in firstNums):
            numContains+=1

print(numContains)