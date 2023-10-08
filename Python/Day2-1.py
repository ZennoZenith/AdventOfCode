ROCK = "ROCK"
PAPER = "PAPER"
SCISSOR = "SCISSOR"


def WhoWon(opponentChoice, playerChoice):
    DRAW = 3
    OPPONENT_WON = 0
    PLAYER_WON = 6
    if opponentChoice == playerChoice:
        return DRAW
    if opponentChoice == ROCK:
        if playerChoice == PAPER:
            return PLAYER_WON
        if playerChoice == SCISSOR:
            return OPPONENT_WON

    elif opponentChoice == PAPER:
        if playerChoice == SCISSOR:
            return PLAYER_WON
        if playerChoice == ROCK:
            return OPPONENT_WON

    elif opponentChoice == SCISSOR:
        if playerChoice == ROCK:
            return PLAYER_WON
        if playerChoice == PAPER:
            return OPPONENT_WON

    return DRAW


def CalculatePoints(opponentChoice, playerChoice):
    normalizationOfChoice = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSOR,
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSOR
    }

    choiceToPoints = {
        ROCK: 1,
        PAPER: 2,
        SCISSOR: 3
    }
    points = WhoWon(
        normalizationOfChoice[opponentChoice],
        normalizationOfChoice[playerChoice])

    points += choiceToPoints[normalizationOfChoice[playerChoice]]

    return points


def main():
    listOfInputsFile = open("Day2.txt", "r")

    listOfInputs = listOfInputsFile.readlines()

    totalPoints = 0
    for inputs in listOfInputs:
        inp = inputs.strip().split(" ")
        totalPoints += CalculatePoints(inp[0].strip(), inp[1].strip())

    listOfInputsFile.close()

    print(totalPoints)


if __name__ == "__main__":
    main()
