scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

opening = ["(", "[", "{", "<"]
matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

f = open("./Puzzel_files/puzzel_10.txt")
input = f.readline().strip()

total_score = 0

while input != "":
    chars = []

    for c in input:
        if c in opening:
            chars.append(c)
        else:
            t = chars.pop()
            if matches[t] != c:
                total_score += scores[c]
    input = f.readline().strip()

print("Part1: ", total_score)