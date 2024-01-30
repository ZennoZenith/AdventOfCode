def CheckIfUnique(arr):
    arrSet = set(arr)
    return len(arrSet) == len(arr)

def main():
    file = open('Day6.txt', "r")
    fileContent = file.readline()
    file.close()

    arr = [fileContent[0],fileContent[1],fileContent[2],fileContent[3]]

    for i in range(4, len(fileContent)):
        if CheckIfUnique(arr):
            print(i)
            break
        arr.append(fileContent[i])
        arr.pop(0)



if __name__ == "__main__":
    main()
