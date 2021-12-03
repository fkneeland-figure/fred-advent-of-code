def part1():
    f = open("./Puzzel_files/puzzel_3.txt")
    line = f.readline().strip()
    length = len(line)
    counts = [0] * length
    print(counts)
    print("------")
    print(line)
    print("-------")
    count = 0

    while line != None and line != "":
        count += 1
        idx = 0
        for l in line:
            if l == "1":
                counts[idx] += 1
            idx += 1

        line = f.readline().strip()

    alpha = 0
    gamma = 0

    print("Count: ", count)
    print("Counts: ", counts)

    idx = 0
    for c in counts:
        idx += 1
        if c > count/2:
            alpha += 2 ** (length - idx)
        else:
            gamma += 2 ** (length - idx)

    print("gamma:", gamma)
    print("alpha: ", alpha)
    print("Part 1 result: ", alpha * gamma)


def str_bin_to_dec(numb):
    length = len(numb)
    idx = 0
    dec = 0
    for n in numb:
        idx += 1
        if n == "1":
            dec += 2 ** (length - idx)

    return dec


def part2():
    f = open("./Puzzel_files/puzzel_3.txt")
    line = f.readline().strip()
    length = len(line)
    counts = [0] * length
    count = 0
    lines = []

    while line != None and line != "":
        lines.append(line)
        if line[0] == "1":
            count += 1
        line = f.readline().strip()

    o_lines = lines.copy()
    c_lines = lines

    idx = 0
    while len(o_lines) > 1:
        ones = []
        zeros = []
        for line in o_lines:
            if line[idx] == "0":
                zeros.append(line)
            else:
                ones.append(line)
        if len(zeros) > len(ones):
            o_lines = zeros
        else:
            o_lines = ones
        idx += 1

    idx = 0
    while len(c_lines) > 1:
        ones = []
        zeros = []
        for line in c_lines:
            if line[idx] == "0":
                zeros.append(line)
            else:
                ones.append(line)
        if len(ones) < len(zeros):
            c_lines = ones
        else:
            c_lines = zeros
        idx += 1

    highest_o = o_lines[0]
    highest_c = c_lines[0]



    print(highest_o)
    print(highest_c)
    o_val = int(str_bin_to_dec(highest_o))
    c_val = int(str_bin_to_dec(highest_c))


    print("Part 2: ", o_val * c_val)


part1()
part2()