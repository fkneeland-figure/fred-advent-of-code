def part1():
    f = open("./Puzzel_files/puzzel_2.txt")
    line = f.readline()
    horizontal = 0
    vertical = 0

    while line is not None and line != "":
        vals = line.split(" ")
        if vals[0] == "forward":
            horizontal += int(vals[1])
        elif vals[0] == "up":
            vertical -= int(vals[1])
        else:
            vertical += int(vals[1])
        line = f.readline()

    print("First part: ", horizontal, ", ", vertical, " combined: ", horizontal * vertical)

def part2():
    f = open("./Puzzel_files/puzzel_2.txt")
    line = f.readline()
    horizontal = 0
    vertical = 0
    aim = 0

    while line is not None and line != "":
        vals = line.split(" ")
        if vals[0] == "forward":
            horizontal += int(vals[1])
            vertical += aim * int(vals[1])
        elif vals[0] == "up":
            aim -= int(vals[1])
        else:
            aim += int(vals[1])
        line = f.readline()

    print("Second part: ", horizontal, ", ", vertical, " combined: ", horizontal * vertical)

part1()
part2()