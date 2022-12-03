f = open('input.txt', 'r')
content = f.read()

SpaceList = content.split('\n')
NoSpaceList = []
points = 0

lose = {
    'A': 3,
    'B': 1,
    'C': 2
}

tie = {
    'A': 1,
    'B': 2,
    'C': 3
}

win = {
    'A': 2,
    'B': 3,
    'C': 1
}


for thing in SpaceList:
    thing = thing.replace(" ", "")
    NoSpaceList.append(thing)

res1 = list(map(lambda st: str.replace(st, "X", "A"), NoSpaceList))
res2 = list(map(lambda st: str.replace(st, "Y", "B"), res1))
res3 = list(map(lambda st: str.replace(st, "Z", "C"), res2))

#print(res3)

for combo in res3:
    # need to lose
    if combo[1] == 'A':
        points += lose.get(combo[0])
    # need to tie
    if combo[1] == 'B':
        points += 3 + tie.get(combo[0])
    # need to win
    if combo[1] == 'C':
        points += 6 + win.get(combo[0])

print (points)