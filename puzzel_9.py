f = open("./Puzzel_files/puzzel_9.txt")

rows = []

row = f.readline().strip()

while row != "":
    rows.append(row)
    row = f.readline().strip()

print(len(rows))

low_points = []
current_low_point = 1
basins = [[0] * len(rows[0]) for _ in range(len(rows))]

for i in range(len(rows)):
    for j in range(len(rows[i])):
        t = int(rows[i][j])

        if t == 9:
            basins[i][j] = -1

        if i > 0 and int(rows[i-1][j]) <= t:
            continue

        if (i+1) < len(rows) and int(rows[i+1][j]) <= t:
            continue

        if j > 0 and int(rows[i][j-1]) <= t:
            continue

        if (j + 1) < len(rows[i]) and int(rows[i][j+1]) <= t:
            continue

        # we need to calculate the basin size...
        basins[i][j] = current_low_point
        current_low_point += 1
        low_points.append(t)

updates = True
rounds = 0

print("------------------")
for row in basins:
    print(row)
print("------------------")

while updates:
    rounds += 1
    updates = False
    for i in range(len(basins)):
        for j in range(len(basins[i])):
            if basins[i][j] == 0:
                updates = True

                if i > 0 and basins[i-1][j] > 0:
                    basins[i][j] = basins[i-1][j]
                if (i+1) < len(basins) and basins[i+1][j] > 0:
                    basins[i][j] = basins[i+1][j]

                if j > 0 and basins[i][j-1] > 0:
                    basins[i][j] = basins[i][j-1]
                if (j+1) < len(basins[i]) and basins[i][j+1] > 0:
                    basins[i][j] = basins[i][j+1]

print("rounds: ", rounds)
basin_sizes = [0] * current_low_point

for i in range(len(basins)):
    for j in range(len(basins[i])):
        if basins[i][j] != -1:
            basin_sizes[basins[i][j]] += 1

top_three = [0, 0, 0, 0]

for numb in basin_sizes:
    top_three[3] = numb
    top_three.sort(reverse=True)

for row in basins:
    print(row)

print(top_three)
# print(len(low_points))
# print(low_points)

sum = 0

for t in low_points:
    sum += 1 + t

print("Part1: ", sum)
print("Part2: ", (top_three[0] * top_three[1] * top_three[2]))

