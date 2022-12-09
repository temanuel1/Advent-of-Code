import numpy

with open('input.txt') as f:
    data = f.readlines()


def solve(v):
    visited = {(0, 0)}
    rope = numpy.zeros((v, 2))

    for move in data:
        d, length = move.split()

        for _ in range(int(length)):
            # move head
            rope[0] += {
                'L': (0, -1), 'R': (0, 1),
                'U': (1, 0), 'D': (-1, 0)
            }[d]

            # move tail
            for i in range(1, len(rope)):
                diff = rope[i - 1] - rope[i]

                if numpy.linalg.norm(diff) >= 2:
                    rope[i] += numpy.sign(diff)

            visited.add(tuple(rope[len(rope) - 1]))

    return len(visited)


print('Part 1:', solve(2))
print('Part 2:', solve(10))