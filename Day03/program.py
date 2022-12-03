with open("Day03\\input") as f:
    lines = f.read().split("\n")

lines.remove("")

def get_common_letter(string_a, string_b):
    common = []
    for char in string_a:
        if char in string_b:
            common.append(char)
    return remove_duplicates(common)

def get_common_letter_three(array):
    first, second, third = array
    c1 = get_common_letter(first, second)
    c2 = get_common_letter(second, third)
    c3 = get_common_letter(c1, c2)
    return c3

def remove_duplicates(array):
    single = []
    for item in array:
        if item not in single: single.append(item)
    return single

d = {}
for line in lines:
    first, second = line[:int(len(line)/2)], line[int(len(line)/2):]
    cl = remove_duplicates(get_common_letter(first, second))
    for c in cl:
        if not d.get(c): d[c] = 0
        d[c] += 1

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_sum = 0
for k in d.keys():
    total_sum += (alphabet.index(k) + 1) * d[k]

print(total_sum) # Answer 1

d = {}
for first_line in range(0, len(lines), 3):
    three = lines[first_line:first_line+3]

    first, second = line[:int(len(line)/2)], line[int(len(line)/2):]
    cl = remove_duplicates(get_common_letter_three(three))
    for c in cl:
        if not d.get(c): d[c] = 0
        d[c] += 1

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_sum = 0
for k in d.keys():
    total_sum += (alphabet.index(k) + 1) * d[k]

print(total_sum) # Answer 2