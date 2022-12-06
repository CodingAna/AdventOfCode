with open("Day06\\input") as f:
    line = f.read().split("\n")[0]

def contains_duplicate(string: str):
    for char in string:
        if string.count(char) > 1: return True
    return False

last_four = ""
counter = 0
for char in line:
    counter += 1
    last_four += char
    if len(last_four) > 4: last_four = last_four[1:]
    if len(last_four) >= 4 and not contains_duplicate(last_four): break

print(counter) # Answer 1

last_fourteen = ""
counter = 0
for char in line:
    counter += 1
    last_fourteen += char
    if len(last_fourteen) > 14: last_fourteen = last_fourteen[1:]
    if len(last_fourteen) >= 14 and not contains_duplicate(last_fourteen): break

print(counter) # Answer 2
