inputFile = open("Day1.txt", "r")

linesInFile = inputFile.readlines()

max = 0
current = 0
for line in linesInFile:
    if line == "\n":
        if current > max:
            max = current
        current = 0
        continue
    current += int(line.strip())

print(max)

inputFile.close()
