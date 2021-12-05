class Board:
    numbers = []
    scores = []
    chosen = []
    round = 0
    last_numb = 0

    def __init__(self, scores, numbers):
        self.scores = scores
        self.numbers = numbers

        self.chosen = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]

    def calculate_round(self):
        count = 0
        for i in range(len(self.numbers)):
            if self.record_numb(self.numbers[i]):
                count += 1

            if count > 5 and self.won():
                self.last_numb = int(self.numbers[i])
                return i+1

        return len(self.numbers)

    def record_numb(self, numb):
        for i in range(len(self.scores)):
            for j in range(len(self.scores[i])):
                if self.scores[i][j] == numb:
                    self.chosen[i][j] = True
                    return True
        return False

    def won(self):
        # check rows:
        for i in range(len(self.chosen)):
            any_false = False
            for j in range(len(self.chosen[i])):
                if self.chosen[i][j] is False:
                    any_false = True
                    break
            if any_false is False:
                return True

        # check columns
        for j in range(len(self.chosen[0])):
            any_false = False
            for i in range(len(self.chosen)):
                if self.chosen[i][j] is False:
                    any_false = True
                    break
            if any_false is False:
                return True

        return False

    def get_score(self):
        total_score = 0
        for i in range(len(self.scores)):
            for j in range(len(self.scores[i])):
                if self.chosen[i][j] is False:
                    total_score += int(self.scores[i][j])
        print("total_score: ", total_score)
        print("lastNumb: ", self.last_numb)
        return total_score * self.last_numb

def part1():
    f = open("./Puzzel_files/puzzel_4.txt")
    numbers = f.readline().strip().split(",")
    f.readline()

    Boards = []
    idx = 0

    done = False

    while not done:
        scores = []

        for i in range(5):
            new_line = f.readline().strip()
            if new_line == "":
                done = True
                break
            score = new_line.split(" ")
            while len(score) > 5:
                score.remove("")
            scores.append(score)

        if not done:
            Boards.append(Board(scores, numbers))
            idx += 1

        # get empty line between boards
        f.readline()

    fastest = len(numbers)
    lowest = 0
    l_board = Boards[0]
    board = Boards[0]
    print(len(numbers))
    print("scores:")
    for b in Boards:
        temp = b.calculate_round()
        print(temp)

        if temp > lowest:
            lowest = temp
            l_board = b

        if temp < fastest:
            board = b
            fastest = temp

    print("-----")
    print(fastest)
    print(board.scores)
    print(board.chosen)
    print("Part 1: ", board.get_score())
    print("Part 2: ", l_board.get_score())

part1()