def CheckIntersection(startIndex1, endIndex1, startIndex2, endIndex2):
    if startIndex1 > startIndex2:
        temp = startIndex1
        startIndex1 = startIndex2
        startIndex2 = temp
        temp = endIndex1
        endIndex1 = endIndex2
        endIndex2 = temp

    if startIndex1 == startIndex2:
        return 2
    if startIndex2 >= startIndex1 and endIndex2 <= endIndex1:
        return 2
    if startIndex2 >= startIndex1 and endIndex2 <= endIndex1:
        return 2
    if startIndex2 <= endIndex1:
        return 1
    return 0


def main():
    file = open("Day4.txt", "r")
    pairText = file.readlines()
    file.close()

    sum = 0
    for pair in pairText:
        pairList = pair.strip().split(",")
        pair1 = pairList[0].split("-")
        pair2 = pairList[1].split("-")
        # Day 4 part 1
        # if 2 == CheckIntersection(

        # Day 4 part 2
        if 0 < CheckIntersection(
                int(pair1[0]),
                int(pair1[1]),
                int(pair2[0]),
                int(pair2[1])):
            # print(pair1, pair2)
            sum += 1

    print(sum)
    return sum


if __name__ == "__main__":
    main()
