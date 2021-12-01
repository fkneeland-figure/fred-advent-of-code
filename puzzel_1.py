
def part1():
    f = open("./Puzzel_files/puzzel_1.txt")
    pastLine = f.readline()
    line = f.readline()
    count = 0

    while line is not None and line != "":
        if int(pastLine) < int(line):
            count = count + 1
        pastLine = line
        line = f.readline()

    print("First part: ", count)


def part2():
    f = open("./Puzzel_files/puzzel_1.txt")
    a = f.readline()
    b = f.readline()
    c = f.readline()
    d = f.readline()
    count = 0

    while d is not None and d != "":
        first = int(a) + int(b) + int(c)
        second = int(b) + int(c) + int(d)
        if second > first:
            count += 1
        a = b
        b = c
        c = d
        d = f.readline()

    print("Second part:")
    print(count)


part1()
part2()
