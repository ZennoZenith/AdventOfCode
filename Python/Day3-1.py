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

    for items in rucksacks:
        stripedItem = items.strip()
        length = len(stripedItem)
        compartments = [
            stripedItem[0:int(length/2)], stripedItem[int(length/2):]]

        commonCharacter = set()

        for character in compartments[0]:
            if compartments[1].find(character) != -1:
                commonCharacter.add(character)

        for character in commonCharacter:
            sum += CalculatePriority(character)

    print(sum)


if __name__ == "__main__":
    main()
