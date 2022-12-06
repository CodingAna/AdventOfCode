with open("Day05\\input") as f:
    lines = f.read().split("\n")

def remove(array: list, value) -> list:
    out = []
    for v in array:
        if v != value:
            out.append(v)
    return out

stack = []
temp_stack = []
i = 0
for line in lines:
    if line == "": break

    temp_line = []
    for j in range(0, len(line), 4): temp_line.append(line[j+1])
    temp_stack.append(temp_line)
    i += 1

for i in range(9):
    col = []
    height = 0
    while temp_stack[height][i] != str(i+1):
        col.insert(0, temp_stack[height][i])
        height += 1
    stack.append(remove(col, " "))

i += 2
lines = lines[i:]
temp_instructions = [line.split(" ") for line in lines]
instructions = []
for ins in temp_instructions:
    instructions.append(remove([int(ins[i]) if i % 2 == 1 else None for i in range(len(ins))], None))

for ins in instructions:
    if ins == []: continue
    count, stack_from, stack_to = ins
    stack_from -= 1
    stack_to -= 1
    counter = 0
    for i in range(len(stack[stack_from])-1, -1, -1):
        if counter >= count: break
        stack[stack_to].append(stack[stack_from][i])
        stack[stack_from][i] = " "
        counter += 1
    stack[stack_from] = remove(stack[stack_from], " ")

print("".join(stack[i][-1] if len(stack[i]) > 0 else "-" for i in range(len(stack)))) # Answer 1

with open("Day05\\input") as f:
    lines = f.read().split("\n")

stack = []
temp_stack = []
i = 0
for line in lines:
    if line == "": break

    temp_line = []
    for j in range(0, len(line), 4): temp_line.append(line[j+1])
    temp_stack.append(temp_line)
    i += 1

for i in range(9):
    col = []
    height = 0
    while temp_stack[height][i] != str(i+1):
        col.insert(0, temp_stack[height][i])
        height += 1
    stack.append(remove(col, " "))

i += 2
lines = lines[i:]
temp_instructions = [line.split(" ") for line in lines]
instructions = []
for ins in temp_instructions:
    instructions.append(remove([int(ins[i]) if i % 2 == 1 else None for i in range(len(ins))], None))

for ins in instructions:
    if ins == []: continue
    count, stack_from, stack_to = ins
    stack_from -= 1
    stack_to -= 1
    for i in range(len(stack[stack_from])):
        if i >= count: break
        i = i + len(stack[stack_from]) - count
        stack[stack_to].append(stack[stack_from][i])
        stack[stack_from][i] = " "
    stack[stack_from] = remove(stack[stack_from], " ")

print("".join(stack[i][-1] if len(stack[i]) > 0 else "-" for i in range(len(stack)))) # Answer 2
