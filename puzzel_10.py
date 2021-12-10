scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

scores2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
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

scores = []

while input != "":
    chars = []
    incomplete = True

    for c in input:
        if c in opening:
            chars.append(c)
        else:
            t = chars.pop()
            if matches[t] != c:
                incomplete = False
                break

    if incomplete and len(chars) > 0:
        score = 0
        for i in range(len(chars)):
            score *= 5
            score += scores2[chars[len(chars)-1-i]]
        print("Score: ", score)
        scores.append(score)

    input = f.readline().strip()

scores.sort()

print(scores)
print("Part 2: ", scores[int(len(scores)/2)])