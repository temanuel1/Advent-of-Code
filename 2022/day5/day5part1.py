f = open('input.txt', 'r')
content = f.readlines()
num_stacks = int(len(content[0]) / 4)
stacks = [[] for i in range(num_stacks)]
end_result = []

for line in content:
    if line[1] == '1':
        break
    for stack in range(num_stacks):
        box_index = 4 * stack + 1
        if line[box_index] == ' ':
            continue
        stacks[stack].append(line[box_index])

class stack:
    boxes = []
    def __init__(self):
        self.boxes = stacks
    def move(self, amount, starting_stack, ending_stack):
        movers = self.boxes[starting_stack-1][:amount][::-1]
        self.boxes[starting_stack-1] = self.boxes[starting_stack-1][amount:]
        self.boxes[ending_stack - 1] = movers + self.boxes[ending_stack - 1]
    def print_top_cargo(self):
        for stack in self.boxes:
            print(stack[0], end='')
    
# Initialize cargo object and call move function based on each command
cargo = stack()
for line in content:
    if line[0] == 'm':
        parts = line.split(' ')
        parts[5] = parts[5][0]
        cargo.move(int(parts[1]), int(parts[3]), int(parts[5]))

cargo.print_top_cargo()