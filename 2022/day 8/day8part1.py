f = open('input.txt', 'r')
content = f.read()
lines = content.split('\n')

width = len(lines[0])
length = (len(lines))
visible = (width * 2) + (length * 2 - 4)

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

    if all(item < height for item in lefts):
        return True
    if all(item < height for item in rights):
        return True
    if all(int(item) < height for item in ups):
        return True
    if all(int(item) < height for item in downs):
        return True
    return False

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i != 0 and i != (len(lines) - 1) and j != 0 and j != (len(lines[0]) - 1):
            height = int(lines[i][j])
            if(check_visibility(height, i, j)):
                visible += 1
            
print(visible)