from os import sep

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
    indexOne = minMax[0]
    indexTwo = minMax[1]
    if sequence[int(indexOne) - 1] == letter and sequence[int(indexTwo) - 1] != letter:
        valids += 1
    elif sequence[int(indexOne) - 1] != letter and sequence[int(indexTwo) - 1] == letter:
        valids += 1
    else:
        valids += 0
    
        

print("There are " + str(valids) + ' valid passwords.')