# Helper function for part 1
def add_surrounding(i, j, vals, flashed):
    for i2 in range(3):
        for j2 in range(3):
            i3 = i-1+i2
            j3 = j-1+j2
            if 0 <= i3 < len(vals) and 0 <= j3 < len(vals[i3]):
                vals[i3][j3] += 1
                if flashed[i3][j3] is False and vals[i3][j3] > 9:
                    flashed[i3][j3] = True
                    add_surrounding(i3, j3, vals, flashed)

f = open("./Puzzel_files/puzzel_11.txt")
input = f.readline().strip()

vals = []
flashed = []
idx = 0

while input != "":
    vals.append([])
    flashed.append([])
    for c in input:
        vals[idx].append(int(c))
        flashed[idx].append(False)
    idx += 1
    input = f.readline().strip()

flashes = 0
all = len(vals) * len(vals[0])
done = False
rounds = 0

while done is False:
    flashes = 0
    rounds += 1
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            vals[i][j] += 1

            if flashed[i][j] is False and vals[i][j] > 9:
                flashed[i][j] = True
                add_surrounding(i, j, vals, flashed)

    for i in range(len(flashed)):
        for j in range(len(flashed[i])):
            if flashed[i][j] is True:
                flashed[i][j] = False
                vals[i][j] = 0
                flashes += 1

    if flashes == all:
        done = True

print("Part 1: ", flashes)
print("Part 2: ", rounds)
