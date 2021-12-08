f = open("./Puzzel_files/puzzel_8.txt")

inputs = []
outputs = []

line = f.readline().strip()

while line != "":
    vals = line.split("|")
    inputs.append(vals[0].strip())
    outputs.append(vals[1].strip())
    line = f.readline().strip()

count = 0

for o in outputs:
    temp = o.split(" ")
    for t in temp:
        if len(t) == 2 or len(t) == 4 or len(t) == 7 or len(t) == 3:
            count += 1

print(outputs)
print("part 1: ", count)


def get_mapping(inputs):
    strs = inputs.split(" ")
    new_mappings = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    mappings = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]

    # get known mappings
    for s in strs:
        if len(s) == 2:
            new_mappings[1] = s
        elif len(s) == 4:
            new_mappings[4] = s
        elif len(s) == 3:
            new_mappings[7] = s
        elif len(s) == 7:
            new_mappings[8] = s

    four = new_mappings[4]

    # get other mappings
    for s in strs:
        if len(s) == 5:
            temp = s
            if new_mappings[1][0] in s and new_mappings[1][1] in s:
                new_mappings[3] = s
            elif len(temp.replace(four[0], "").replace(four[1], "").replace(four[2], "").replace(four[3], "")) == 2:
                new_mappings[5] = s
            else:
                new_mappings[2] = s
        elif len(s) == 6:
            if four[0] in s and four[1] in s and four[2] in s and four[3] in s:
                new_mappings[9] = s
            elif new_mappings[1][0] in s and new_mappings[1][1] in s:
                new_mappings[0] = s
            else:
                new_mappings[6] = s
    return new_mappings

def get_value(mapping, inputs):
    numb = 0
    strs = inputs.split(" ")

    for s in strs:
        numb *= 10
        temp = sorted(s)
        l = len(temp)
        for i in range(10):
            if len(mapping[i]) == l and sorted(mapping[i]) == temp:
                numb += i
                break

    return numb

# m = get_mapping("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab")
# print(get_value(m, "cdfeb fcadb cdfeb cdbaf"))

total_sum = 0
for i in range(len(inputs)):
    m = get_mapping(inputs[i])
    total_sum += get_value(m, outputs[i])

print("Part 2: ", total_sum)

