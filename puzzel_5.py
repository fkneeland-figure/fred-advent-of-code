class Row:
    p1x = 0
    p1y = 0
    p2x = 0
    p2y = 0

    def __init__(self, str):
        str = str.replace(" -> ", ",")
        strs = str.split(",")
        self.p1x = int(strs[0])
        self.p1y = int(strs[1])
        self.p2x = int(strs[2])
        self.p2y = int(strs[3])

    def is_legal(self):
        return self.p1x == self.p2x or self.p1y == self.p2y or self.is_diagonal()

    def is_diagonal(self):
        return abs(self.p1y - self.p2y) == abs(self.p1x - self.p2x)

    def min_x(self):
        if self.p1x < self.p2x:
            return self.p1x
        return self.p2x

    def min_x_y(self):
        if self.p1x < self.p2x:
            return self.p1y
        return self.p2y

    def positive_y(self):
        return self.min_x_y() < self.max_y()

    def max_x(self):
        if self.p1x > self.p2x:
            return self.p1x
        return self.p2x

    def min_y(self):
        if self.p1y < self.p2y:
            return self.p1y
        return self.p2y

    def max_y(self):
        if self.p1y > self.p2y:
            return self.p1y
        return self.p2y


f = open("./Puzzel_files/puzzel_5.txt")

row = f.readline().strip()
rows = []
count = 0

max_x = 0
max_y = 0

while len(row) > 0:
    temp = Row(row)

    if temp.is_legal():
        rows.append(temp)

        if temp.max_y() > max_y:
            max_y = temp.max_y()
        if temp.max_x() > max_x:
            max_x = temp.max_x()

    count += 1
    row = f.readline().strip()

print("Count: ", count)
print("Rows: ", len(rows))
print("Max x: ", max_x)
print("Max y: ", max_y)


grid = [ [0]*max_y for i in range(max_x)]

print("len: ", len(grid))
print("2 len: ", len(grid[0]))

for row in rows:
    if row.is_diagonal():
        i = row.min_x() - 1
        j = row.min_x_y() - 1

        while i != row.max_x():
            grid[i][j] += 1

            i += 1
            if row.positive_y():
                j += 1
            else:
                j -= 1

    else:
        for i in range(row.min_x()-1, row.max_x()):
            for j in range(row.min_y()-1, row.max_y()):
                grid[i][j] += 1

count = 0
for row in grid:
    for p in row:
        if p > 1:
            count += 1

print(count)

