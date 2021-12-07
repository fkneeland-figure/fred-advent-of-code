from math import floor, ceil

def part1():
    f = open("./Puzzel_files/puzzel_7.txt")
    inputs = f.readline().strip().split(",")

    avg = 0

    sorted = [0] * len(inputs)

    for i in range(len(inputs)):
        sorted[i] = int(inputs[i])

    sorted.sort()

    avg = sorted[int(len(inputs)/2)]

    cost_1 = 0
    cost_2 = 0

    for numb in sorted:
        cost_1 += abs(floor(avg) - int(numb))
        cost_2 += abs(ceil(avg) - int(numb))

    print("cost_1: ", cost_1)
    print("cost_2: ", cost_2)


def part2():
    f = open("./Puzzel_files/puzzel_7.txt")
    inputs = f.readline().strip().split(",")

    max = 0
    avg = 0

    for n in inputs:
        avg += int(n)
        if int(n) > max:
            max = int(n)

    avg = int(avg / len(inputs))
    print("avg: ", avg)
    print("max: ", max)

    costs = [0]

    for i in range(1, int(max-avg)+1):
        costs.append(costs[i-1]+i)
    print(costs)

    total_cost = 0
    total_cost2 = 0

    for n in inputs:

        cost = costs[abs(avg-int(n))]
        print("n: ", n, " distance: ", abs(avg - int(n)), " cost: ", cost)
        total_cost += cost
        cost2 = costs[abs((avg+1)-int(n))]
        total_cost2 += cost2

    print("cost: ", total_cost)
    print("cost2: ", total_cost2)



# part1()
part2()
