def CalculatePriority(character):
    val = ord(character)
    if val >= ord('A') and val <= ord('Z'):
        val += 27 - ord('A')
    elif val >= ord('a') and val <= ord('z'):
        val += 1 - ord('a')
    return val


def main():
    file = open("Day3.txt", "r")
    rucksacks = file.readlines()
    file.close()

    sum = 0

    for index in range(0, len(rucksacks), 3):
        stripedItem = rucksacks[index].strip()
        sets = set()
        sets2 = set()
        for character in stripedItem:
            sets.add(character)

        stripedItem = rucksacks[index+1].strip()
        for character in stripedItem:
            sets2.add(character)

        sets = sets.intersection(sets2)
        sets2.clear()
        stripedItem = rucksacks[index+2].strip()

        for character in stripedItem:
            sets2.add(character)

        sets = sets.intersection(sets2)

        sum += CalculatePriority(sets.pop())

    print(sum)
    return sum


if __name__ == "__main__":
    main()
