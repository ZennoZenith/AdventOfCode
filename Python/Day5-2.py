def Move(stacks, fromIndex, toIndex, times):
    temp = []
    for i in range(0, times):
        try:
            temp.append(stacks[fromIndex - 1].pop())
        except IndexError:
            print("Underflow")
    for i in range(0, times):
        stacks[toIndex - 1].append(temp.pop())


def main():
    file = open("Day5.txt", "r")
    lines = file.readlines()
    file.close()

    numberOfColumns = int(len(lines[0]) / 4)

    matrix = []
    stacks = []
    for i in range(0, numberOfColumns):
        matrix.append([])
        stacks.append([])

    i = 0
    while (i < len(lines)):
        if lines[i].find('[') == -1:
            break
        for index in range(0, numberOfColumns):
            matrix[i].append(lines[i][index*4+1])
        # print(matrix[i])
        i += 1

    numberOfRows = i

    for index in range(0, numberOfColumns):
        for row in range(numberOfRows - 1, -1, -1):
            if (matrix[row][index] == ' '):
                break
            stacks[index].append(matrix[row][index])
        # print(stacks[index])

    i += 2
    while (i < len(lines)):
        strSplit = lines[i].strip().split(' ')
        numberOfTimes = int(strSplit[1])
        fromIndex = int(strSplit[3])
        toIndex = int(strSplit[5])
        Move(stacks, fromIndex, toIndex, numberOfTimes)
        i += 1

    finalAns = ""
    for index in range(0, numberOfColumns):
        finalAns += stacks[index].pop()
        # print(stacks[index])

    print("Final Ans: " + finalAns)


if __name__ == "__main__":
    main()
