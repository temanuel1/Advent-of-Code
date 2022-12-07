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

for k, v in SZ.items():
    #print(k, v)
    if v <= 100000:
        ans += v
    
print(ans)