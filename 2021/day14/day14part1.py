f = open('2021/day14/input.txt', 'r')
content = f.read()
##print(content)
updatedList = content.split("\n")

startingPolymer = updatedList[0]

def split(word):
    return list(word)     
charsinPolymer = split(startingPolymer)

keys = []
values = []
instanceIndexes = []
dictIndexes = []


setup = dict()


for i in range(1, len(updatedList)):
    polymerTemplate = updatedList[i].split(" -> ")

    setup[polymerTemplate[0]] = polymerTemplate[1]
    keys.append(polymerTemplate[0])
    values.append(polymerTemplate[1])


def indexFinder():
    for i in range(len(charsinPolymer) - 1):
        if(charsinPolymer[i] + charsinPolymer[i+1] in keys):
            index = keys.index(charsinPolymer[i] + charsinPolymer[i+1])
            dictIndexes.append(index)
            instanceIndexes.append(i + 1)

def pairInsertion():
    c = 0
    while c < 10:
        indexFinder()
        for i in range(len(instanceIndexes)):
            charsinPolymer.insert(instanceIndexes[i] + i, values[dictIndexes[i]])
        instanceIndexes.clear()
        dictIndexes.clear()
        c += 1

def minMax():
    b = 0
    c = 0
    f = 0
    h = 0
    k = 0
    n = 0
    o = 0
    p = 0
    s = 0
    v = 0
    nums = []
    for char in charsinPolymer:
        ## Need to acc for diff letters
        if char == 'B':
            b += 1
        elif char == 'C':
            c += 1
        elif char == 'F':
            f += 1
        elif char == 'H':
            h += 1
        elif char == 'K':
            k += 1
        elif char == 'N':
            n += 1
        elif char == 'O':
            o += 1
        elif char == 'P':
            p += 1
        elif char == 'S':
            s += 1
        else:
            v += 1
    nums.append(b)
    nums.append(c)
    nums.append(f)
    nums.append(h)
    nums.append(k)
    nums.append(n)
    nums.append(o)
    nums.append(p)
    nums.append(s)
    nums.append(v)
    nums.sort()
    return nums[len(nums) - 1] - nums[0]


pairInsertion()
print("Answer is: " + str(minMax()))