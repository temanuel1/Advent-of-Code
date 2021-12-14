from functools import total_ordering


data = []
with open("2021/day8/input.txt") as file:
    line = file.readline()
    while line:
        left = sorted(["".join(sorted(x)) for x in line.strip("\n").split("|")[0].split()], key=len)
        right = ["".join(sorted(x)) for x in line.strip("\n").split("|")[1].split()]
        data.append([left, right])
        line = file.readline()

def Substring(a, b):
    count = str()
    for char in a:
        if char in b:
            count+=char
    return count

completeTotal = 0

for prob in data:
    ten = prob[0]
    #print(ten)

    # 1, 4, 7, 8
    setup = dict({ten[0]: 1, ten[1]: 7, ten[2]: 4, ten[9]: 8})

    # Three Nums with 5 Segments (3, 2, 5)
    fives = [ten[3], ten[4], ten[5]]
    

    # Three Nums with 6 Segments (6, 9, 0)
    sixes = [ten[6], ten[7], ten[8]]

    #print(fives, sixes)

    # 6
    for i in range(len(sixes)):
        if len(Substring(ten[0], sixes[i])) == 1:
            setup[sixes[i]] = 6
            del(sixes[i])
            break

    # 3
    for i in range(len(fives)):
        if len(Substring(ten[0], fives[i])) == 2:
            setup[fives[i]] = 3
            del(fives[i])
            break
   
   # 9
    for i in range(len(sixes)):
        if len(Substring(ten[2], sixes[i])) == 4:
            setup[sixes[i]] = 9
            del(sixes[i])
            break

    # 0
    setup[sixes[0]] = 0

    # 2
    for i in range(len(fives)):
        if len(Substring(ten[2], fives[i])) == 2:
            setup[fives[i]] = 2
            del(fives[i])
            break

    # 5
    setup[fives[0]] = 5


    total = 0
    for digit in prob[1]:
        total*=10
        total+=setup[digit]
    completeTotal+=total

print("Answer is: " + str(completeTotal))