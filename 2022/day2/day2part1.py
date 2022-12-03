f = open('input.txt', 'r')
content = f.read()

SpaceList = content.split('\n')
NoSpaceList = []
points = 0

beats = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

def play(p1, p2):
    if p1 == p2:
        return 3
    if beats[p1] == p2:
        return 6
    return 0

for thing in SpaceList:
    thing = thing.replace(" ", "")
    NoSpaceList.append(thing)

res1 = list(map(lambda st: str.replace(st, "X", "A"), NoSpaceList))
res2 = list(map(lambda st: str.replace(st, "Y", "B"), res1))
res3 = list(map(lambda st: str.replace(st, "Z", "C"), res2))

for combo in res3:
    if combo[1] == 'A':
        points += 1
    if combo[1] == 'B':
        points += 2
    if combo[1] == 'C':
        points += 3
    points += play(combo[0], combo[1])

print(points)