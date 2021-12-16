f = open('2020/day2/input.txt', 'r')
content = f.read()

lines = content.split("\n")

occurrences = 0
valids = 0

def split(word):
    return list(word)

for line in lines:
    content = line.split(" ")
    letter = content[1].split()
    letterList = str(str(letter).replace(":", ""))
    letter = letterList[2]
    sequence = content[2].split()
    for thing in sequence:
        sequence = thing
    sequence = list(sequence)
    numRange = content[0]
    minMax = numRange.split("-")
    min = minMax[0]
    max = minMax[1]
    for char in sequence:
        if char == letter:
            occurrences += 1
    if occurrences >= int(min) and occurrences <= int(max):
        valids += 1
    occurrences = 0

print("There are " + str(valids) + ' valid passwords.')