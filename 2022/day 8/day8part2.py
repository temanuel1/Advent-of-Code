f = open('input.txt', 'r')
content = f.read()
lines = content.split('\n')

width = len(lines[0])
length = (len(lines))
visible = (width * 2) + (length * 2 - 4)
scores = []

def check_visibility(height, i, j):
    lefts = [int(x) for x in str(lines[i][:j])]
    rights = [int(x) for x in str(lines[i][j+1:])]
    ups = []
    downs = []
    for k in range(i):
        ups.append(lines[k][j])
    down_lines = lines[i+1:]
    for line in down_lines:
        downs.append(line[j])
    lefts_rev, ups_rev = lefts[slice(None, None, -1)], ups[slice(None, None, -1)]

    if all(item < height for item in lefts):
        scores.append(calc_score(height, lefts_rev, rights, ups_rev, downs))
        return True
    if all(item < height for item in rights):
        scores.append(calc_score(height, lefts_rev, rights, ups_rev, downs))
        return True
    if all(int(item) < height for item in ups):
        scores.append(calc_score(height, lefts_rev, rights, ups_rev, downs))
        return True
    if all(int(item) < height for item in downs):
        scores.append(calc_score(height, lefts_rev, rights, ups_rev, downs))
        return True
    return False

def calc_score(height, lefts, rights, ups, downs):
    l, r, u, d = len(lefts), len(rights), len(ups), len(downs)
    for i in range(len(lefts)):
        if (int(lefts[i]) >= int(height)):
            l = i + 1
            break
    for i in range(len(rights)):
        if (int(rights[i]) >= height):
            r = i + 1
            break
    for i in range(len(ups)):
        if (int(ups[i]) >= int(height)):
            u = i + 1
            break
    for i in range(len(downs)):
        if (int(downs[i]) >= height):
            d = i + 1
            break
    return l * r * u * d

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i != 0 and i != (len(lines) - 1) and j != 0 and j != (len(lines[0]) - 1):
            height = int(lines[i][j])
            if(check_visibility(height, i, j)):
                visible += 1
            
print(max(scores))