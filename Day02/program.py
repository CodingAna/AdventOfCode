with open("Day02\\input") as f:
    lines = f.read().split("\n")

def is_draw(op, me):
    if op == "A" and me == "X": return True
    if op == "B" and me == "Y": return True
    if op == "C" and me == "Z": return True
    return False

def make_draw(op):
    me = ""
    if op == "A": me = "X"
    if op == "B": me = "Y"
    if op == "C": me = "Z"
    return me

lines.remove("")

# AX = Stein
# BY = Paper
# CZ = Schere

total_score = 0
for line in lines:
    opponent, me = line.split(" ")
    round_score = 1 if me == "X" else 2 if me == "Y" else 3

    if is_draw(opponent, me): round_score += 3

    if opponent == "A" and me == "Y": round_score += 6
    if opponent == "B" and me == "Z": round_score += 6
    if opponent == "C" and me == "X": round_score += 6

    total_score += round_score

print(total_score) # Answer 1

total_score = 0
for line in lines:
    opponent, my_action = line.split(" ")
    if my_action == "X":
        if opponent == "A": me = "Z"
        if opponent == "B": me = "X"
        if opponent == "C": me = "Y"
    if my_action == "Y": me = make_draw(opponent)
    if my_action == "Z":
        if opponent == "A": me = "Y"
        if opponent == "B": me = "Z"
        if opponent == "C": me = "X"
    round_score = 1 if me == "X" else 2 if me == "Y" else 3

    if is_draw(opponent, me): round_score += 3

    if opponent == "A" and me == "Y": round_score += 6
    if opponent == "B" and me == "Z": round_score += 6
    if opponent == "C" and me == "X": round_score += 6

    total_score += round_score

print(total_score) # Answer 2