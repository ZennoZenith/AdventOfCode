test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def main():
    file = open("day-3-1.txt", "r")
    lines = file.read().split("\n")
    # lines = test.split("\n")
    print(lines[-1])
    file.close()

    row_len = len(lines)
    col_len = len(lines[0])
    print(row_len, col_len)
    total = 0

    for i in range(0, row_len):
        num = 0
        wasNumValid = False
        for j in range(0, col_len):
            if not lines[i][j].isnumeric():
                if wasNumValid:
                    total += num
                num = 0
                wasNumValid = False
                continue

            num = (num * 10) + int(lines[i][j])

            if boxtravel(i, j, lines, row_len, col_len):
                wasNumValid = True

        if wasNumValid:
            total += num

    print(total)


def isSymbol(s: str):
    return not (s.isnumeric() or s == ".")


def isSelf(i, j, a, b):
    return i == a and j == b


def boxtravel(a, b, arr, row_len, col_len):
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if i < 0 or i >= row_len:
                continue
            if j < 0 or j >= col_len:
                continue
            if isSelf(i, j, a, b):
                continue
            if not isSymbol(arr[i][j]):
                continue
            return True
    return False


if __name__ == "__main__":
    main()
