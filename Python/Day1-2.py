def GetLowestIndex(arr):
    if len(arr) == 0:
        return -1

    minIndex = 0
    for index in range(0, len(arr)):
        if arr[index] < arr[minIndex]:
            minIndex = index
    return minIndex


inputFile = open("Day1.txt", "r")

linesInFile = inputFile.readlines()

max = [0, 0, 0]
minIndex = GetLowestIndex(max)
current = 0

for line in linesInFile:
    if line == "\n":
        if current > max[minIndex]:
            max[minIndex] = current
            minIndex = GetLowestIndex(max)
        current = 0
        continue
    current += int(line.strip())

print(max)
print(max[0] + max[1] + max[2])

inputFile.close()
