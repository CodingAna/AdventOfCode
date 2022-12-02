with open("Day01\\input") as f:
    lines = f.read().split("\n")

d = []
i = 0
for line in lines:
    if i == len(d): d.append(0)
    if line == "": i += 1
    else: d[i] += int(line)

d.sort()
print(d[-1]) # Answer 1
print(sum([d[-(x+1)] for x in range(3)])) # Answer 2