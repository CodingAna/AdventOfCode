with open("Day04\\input") as f:
    lines = f.read().split("\n")

lines.remove("")

def array_is_in_array(array1, array2) -> bool:
    for item in array1:
        if not item in array2:
            return False
    return True

def array_is_in_array_any(array1, array2) -> bool:
    for item in array1:
        if item in array2:
            return True
    return False

pairs = 0
for line in lines:
    first, second = line.split(",")

    first = first.split("-")
    second = second.split("-")

    frange = list(range(int(first[0]), int(first[1])+1))
    srange = list(range(int(second[0]), int(second[1])+1))

    f = array_is_in_array(frange, srange)
    s = array_is_in_array(srange, frange)

    if f or s: pairs += 1

print(pairs) # Answer 1

pairs = 0
for line in lines:
    first, second = line.split(",")

    first = first.split("-")
    second = second.split("-")

    frange = list(range(int(first[0]), int(first[1])+1))
    srange = list(range(int(second[0]), int(second[1])+1))

    f = array_is_in_array_any(frange, srange)
    s = array_is_in_array_any(srange, frange)

    if f or s: pairs += 1

print(pairs) # Answer 2