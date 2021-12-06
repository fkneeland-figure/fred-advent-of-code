# we want a tree structure

direct_descendents = [0] * 264

for i in range(1, 264):
    direct_descendents[i] = direct_descendents[i-1]
    if i > 7 and (i - 9) % 7 == 0:
        direct_descendents[i] += 1

print(direct_descendents)

total_descendents = [0] * 264

for i in range(0, 264):
    total_descendents[i] = direct_descendents[i]

    for j in range(direct_descendents[i]):
        # i is your age.  You want the total number of descendents of your child which is i-9-j*7 days old
        total_descendents[i] += total_descendents[(i-9)-(j*7)]

print(total_descendents)

f = open("./Puzzel_files/puzzel_6.txt")

inputs = f.readline().strip().split(",")

total = 0

for numb in inputs:
    total += total_descendents[264-int(numb)]

# print(len(inputs))
print("Total: ", total+len(inputs))



# Brute forcing the solution
# 351092
for i in range(80):
    l = len(inputs)
    next = [0] * l
    idx = 0
    for numb in inputs:
        n = int(numb)
        if n < 1:
            if idx < l-1:
                next[idx] = 6
                idx += 1
                next[idx] = 8
                idx += 1
            else:
                next.append(6)
                next.append(8)

        else:
            if idx < l:
                next[idx] = n-1
                idx += 1
            else:
                next.append(n-1)
    inputs = next

print("Total: ", len(next))