f = open('input.txt', 'r')
content = f.read()

List = content.split('\n')
Cals = []
currentCal = 0
elves = List.count('') + 1


for i in range(elves):
    if '' in List:
        endIndex = List.index('')
        for j in range(endIndex):
            currentCal += int(List[j])
        Cals.append(currentCal)
        List = List[endIndex + 1:]
        currentCal = 0
    else:
        for k in range(len(List)):
            currentCal += int(List[k])
        Cals.append(currentCal)

Cals = sorted(Cals, key=int, reverse=True)

print(Cals[:3])
print(int(Cals[0] + Cals[1] + Cals[2]))