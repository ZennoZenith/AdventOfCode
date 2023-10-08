ROCK = "ROCK"
PAPER = "PAPER"
SCISSOR = "SCISSOR"
DRAW = 3
OPPONENT_WON = 0
PLAYER_WON = 6


def Chosser(opponentChoice, whoShouldWin):
    if whoShouldWin == DRAW:
        return opponentChoice
    if whoShouldWin == OPPONENT_WON:
        if opponentChoice == ROCK:
            return SCISSOR
        if opponentChoice == PAPER:
            return ROCK
        if opponentChoice == SCISSOR:
            return PAPER
    if whoShouldWin == PLAYER_WON:
        if opponentChoice == ROCK:
            return PAPER
        if opponentChoice == PAPER:
            return SCISSOR
        if opponentChoice == SCISSOR:
            return ROCK


def CalculatePoints(opponentChoice, playerChoice):
    normalizationOfChoice = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSOR,
    }

    choiceToPoints = {
        ROCK: 1,
        PAPER: 2,
        SCISSOR: 3
    }

    whoShoudWin = {
        'X': OPPONENT_WON,
        'Y': DRAW,
        'Z': PLAYER_WON
    }

    points = whoShoudWin[playerChoice]

    points += choiceToPoints[Chosser(
        normalizationOfChoice[opponentChoice],
        whoShoudWin[playerChoice])]

    return points


def main():
    listOfInputsFile = open("Day2.txt", "r")

    listOfInputs = listOfInputsFile.readlines()
    listOfInputsFile.close()
    totalPoints = 0
    for inputs in listOfInputs:
        inp = inputs.strip().split(" ")
        totalPoints += CalculatePoints(inp[0].strip(), inp[1].strip())

    listOfInputsFile.close()

    print(totalPoints)


if __name__ == "__main__":
    main()
