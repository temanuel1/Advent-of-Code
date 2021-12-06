from collections import defaultdict

def next_state(state):
    new = defaultdict(int)
    new[7] = state[8]
    new[6] = state[7] + state[0]
    new[5] = state[6]
    new[4] = state[5]
    new[3] = state[4]
    new[2] = state[3]
    new[1] = state[2]
    new[0] = state[1]
    new[8] = state[0]
    return new

numbers = [l.strip() for l in open("2021/day6/nums.txt", "r").readlines()][0].split(',')
state = defaultdict(int)
for n in numbers:
    state[int(n)] += 1

for n in range(0, 256):
    state = next_state(state)

print(sum(state.values()))