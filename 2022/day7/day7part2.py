from collections import defaultdict


f = open('input.txt', 'r')
content = f.read()
lines = content.split('\n')

path = []
SZ = defaultdict(int)

for line in lines:
    #print(path)
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])
        #print(path, sz)
        for i in range(len(path) + 1):
            SZ['/'.join(path[:i])] += sz

ans = 0
best = 1e9
max_used = 40000000
total_used = SZ['/']
need_to_free = total_used - max_used

for k, v in SZ.items():
    if v >= need_to_free:
        best = min(best, v)

print(best)