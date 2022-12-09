f = open('input.txt', 'r')
content = f.read()
lines = content.split('\n')

unqiues = []
head_x, head_y, tail_x, tail_y = 0, 0, 0, 0


for line in lines:
    dir = line[0]
    num = int(line[2:])
    if dir == 'R':
        for i in range(num):
            head_x += 1
            if head_y > tail_y and head_x - tail_x > 1:
                tail_y += 1
                tail_x += 1
            elif head_y < tail_y and head_x - tail_x > 1:
                tail_y -= 1
                tail_x += 1
            elif head_x - tail_x >= 2:
                tail_x += 1
            if not [tail_x, tail_y] in unqiues:
                unqiues.append([tail_x, tail_y])
    if dir == 'L':
        for i in range(num):
            head_x -= 1
            if head_y > tail_y and head_x - tail_x < -1:
                tail_y += 1
                tail_x -= 1
            elif head_y < tail_y and head_x - tail_x < -1:
                tail_y -= 1
                tail_x -= 1
            elif head_x - tail_x <= -2:
                tail_x -= 1
            if not [tail_x, tail_y] in unqiues:
                unqiues.append([tail_x, tail_y])
    if dir == 'U':
        for i in range(num):
            head_y += 1
            if head_x > tail_x and head_y - tail_y > 1:
                tail_x += 1
                tail_y += 1
            elif head_x < tail_x and head_y - tail_y > 1:
                tail_x -= 1
                tail_y += 1
            elif head_y - tail_y >= 2:
                tail_y += 1
            if not [tail_x, tail_y] in unqiues:
                unqiues.append([tail_x, tail_y])
    if dir == 'D':
        for i in range(num):
            head_y -= 1
            if head_x > tail_x and head_y - tail_y < -1:
                tail_x += 1
                tail_y -= 1
            elif head_x < tail_x and head_y - tail_y < -1:
                tail_x -= 1
                tail_y -= 1
            elif head_y - tail_y <= -2:
                tail_y -= 1
            if not [tail_x, tail_y] in unqiues:
                unqiues.append([tail_x, tail_y])

print(len(unqiues))