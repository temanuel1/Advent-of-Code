f = open('input.txt', 'r')
content = f.read()
lines = content.split("\n")
num_monkeys = int((len(lines) - 3) / 6)
all_items = []
steps = []
inspects = []
for i in range(num_monkeys):
    inspects.append(0)

for i in range(num_monkeys):
    items = lines[1 + (7 * i)][16:].split(",")
    for j in range(len(items)):
        items[j] = items[j].strip()
    all_items.append(items)
    steps.append(lines[(2 + i*7):(6 + i * 7)])


class Monkeys:
    # Each monkey is represented by a list within the 2-D List
    items = []
    def __init__(self, all_items):
        self.items = all_items
    def print_monkeys(self):
        print(self.items)

m = Monkeys(all_items)

for l in range(20):
    for i in range(len(steps)):
        change = str(steps[i][0][21:len(steps[i][0])])
        op, num = change.split(" ")[0], change.split(" ")[1]
        div = str(steps[i][1]).split(" ")[3]
        t_monkey = str(steps[i][2]).split(" ")[5]
        f_monkey = str(steps[i][3]).split(" ")[5]
        # For each item the monkey has
        for j in range(len(m.items[i])):
            inspects[i] = inspects[i] + 1
            if op == '*':
                if num == 'old':
                    m.items[i][j] = int(m.items[i][j]) * int(m.items[i][j])
                else:
                    m.items[i][j] = int(m.items[i][j]) * int(num)
            else:
                m.items[i][j] = int(m.items[i][j]) + int(num)
            m.items[i][j] = m.items[i][j] // 3
            if m.items[i][j] % int(div) == 0:
                m.items[int(t_monkey)].append(m.items[i][j])
            else:
                m.items[int(f_monkey)].append(m.items[i][j])
        m.items[i].clear()
m.print_monkeys()

one = max(inspects)
inspects.remove(one)
two = max(inspects)
print(one * two)