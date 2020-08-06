import msvcrt
import random


playerPuck = "X"
opponentPuck = "O"
emptyCell = " "

gameHistory = [0]

pucks = {0: playerPuck, 1: opponentPuck, 2: opponentPuck}

board = [
    emptyCell,    emptyCell,    emptyCell,
    emptyCell,    emptyCell,    emptyCell,
    emptyCell,    emptyCell,    emptyCell,
]

numpadControls = {
    7: "0",    8: "1",    9: "2",
    4: "3",    5: "4",    6: "5",
    1: "6",    2: "7",    3: "8",
}

numBoard = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3"
]

# board with numpad labels. only used once per game
def printNumBoard():
    row_1, row_2, row_3 = [], [], []
    for i in range(0, 3):
        row_1.append(numBoard[i + 0]),
        row_2.append(numBoard[i + 3]),
        row_3.append(numBoard[i + 6])
    print(
        "\n",
        " ║ ".join(row_1),
        "\n",
        "\r═══╬═══╬═══\n",
        " ║ ".join(row_2),
        "\n",
        "\r═══╬═══╬═══\n",
        " ║ ".join(row_3),
        "\n",
    )

# board with updated cells. always used at every turn
def printBoard():
    row_1, row_2, row_3 = [], [], []
    for i in range(0, 3):
        row_1.append(board[i + 0]),
        row_2.append(board[i + 3]),
        row_3.append(board[i + 6])
    print(
        "\n",
        " ║ ".join(row_1),
        "\n",
        "\r═══╬═══╬═══\n",
        " ║ ".join(row_2),
        "\n",
        "\r═══╬═══╬═══\n",
        " ║ ".join(row_3),
        "\n",
    )

# used to clear the board
def resetBoard():
    for i in range(len(board)):
        board[i] = emptyCell

# creates a list of all the board rows
def getBoardRows():
    boardRows = [[], [], []]
    boardRows[0].extend([board[0], board[1], board[2]])
    boardRows[1].extend([board[3], board[4], board[5]])
    boardRows[2].extend([board[6], board[7], board[8]])
    return boardRows

# creates a list of all the board columns
def getBoardCols():
    boardCols = [[], [], []]
    boardCols[0].extend([board[0], board[3], board[6]])
    boardCols[1].extend([board[1], board[4], board[7]])
    boardCols[2].extend([board[2], board[5], board[8]])
    return boardCols

# creates a list of all the board diagonals
def getBoardDiag():
    boardDiag = [[], []]
    boardDiag[0].extend([board[0], board[4], board[8]])
    boardDiag[1].extend([board[2], board[4], board[6]])
    return boardDiag

# checks whether the player attempts to place a move over a filled cell
def checkMoveValidity(boardCell):
    if board[boardCell] != emptyCell:
        print("Invalid move! Cell is already filled!")
        return False
    else:
        return True

# reads player numpad input
def askPlayerInput(puck):
    while True:
        print(puck + "'s turn!\nUse Numpad keys to send your move:")
        playerInput = int(msvcrt.getch())
        boardCell = interpretPlayerInput(playerInput)
        if checkMoveValidity(boardCell):
            registerInput(boardCell, puck)
            break
        else:
            printBoard()

# gives the corresponding cell provided the numpad input
def interpretPlayerInput(playerInput):
    boardCell = int(numpadControls[playerInput])
    return boardCell

# used by the BOT to find and fill an empty cell
def genOpponentInput(puck):
    while True:
        randomCell = random.randint(0, 8)
        if board[randomCell] == emptyCell:
            registerInput(randomCell, puck)
            break

# places the valid move onto an empty cell
def registerInput(boardCell, puck):
    board[boardCell] = puck
    if puck == playerPuck:
        print("Player moves!")
    else:
        print("Opponent moves!")
    printBoard()

# scans the board for empty cells
def checkBoardIfFilled():
    for i in range(len(board)):
        if board[i] == emptyCell:
            return False
    return True

# determines whether a row, column or diagonal contains only pucks
def listEqualCells(boardList, puck):
    for box in boardList:
        if all(cell == puck for cell in box):
            return True
    return False

# sends a list of rows to the listEqualCells function
def checkBoardRows(puck):
    boardRows = getBoardRows()
    if listEqualCells(boardRows, puck):
        return True
    else:
        return False

# sends a list of columbns to the listEqualCells function
def checkBoardCols(puck):
    boardCols = getBoardCols()
    if listEqualCells(boardCols, puck):
        return True
    else:
        return False

# sends a list of diagonals to the listEqualCells function
def checkBoardDiag(puck):
    boardDiag = getBoardDiag()
    if listEqualCells(boardDiag, puck):
        return True
    else:
        return False

# the parent function of the previous three functions above
def checkBoard(puck):
    if checkBoardRows(puck):
        return True
    elif checkBoardCols(puck):
        return True
    elif checkBoardDiag(puck):
        return True
    else:
        return False


def player1Turn():
    puck = playerPuck
    askPlayerInput(puck)


def opponentTurn():
    puck = opponentPuck
    genOpponentInput(puck)


def player2Turn():
    puck = opponentPuck
    askPlayerInput(puck)

# determines whether player 1 will play against a BOT or another player
def askOpponentType():
    while True:
        print("Choose your opponent:  [1] BOT  [2] Player 2")
        opponent = int(msvcrt.getch())

        if opponent == 1:
            print("Opponent: BOT")
            return opponent
        elif opponent == 2:
            print("Opponent: Player 2")
            return opponent
        else:
            print("\nInvalid opponent type! Try again!")

# refers to the game history to ensure that the game turns alternate between the player and the opponent
def getNextTurn(opponent):
    nextTurn = gameHistory[-1]
    if nextTurn == 0:
        gameHistory.append(opponent)
    elif nextTurn == opponent:
        gameHistory.append(0)
    return nextTurn

# calls the next player to play, depending on the current nextTurn value
def nextTurnManager(nextTurn):
    if nextTurn == 0:
        player1Turn()
    elif nextTurn == 1:
        opponentTurn()
    elif nextTurn == 2:
        player2Turn()

# the main game program
while True:
    print("\n\nWelcome to TicTacToe!")
    opponent = askOpponentType()
    printNumBoard()

    while True:

        if checkBoardIfFilled():
            print("Game finished, board is full!")
            break
        else:
            nextTurn = getNextTurn(opponent)
            puck = pucks[nextTurn]
            nextTurnManager(nextTurn)
            if checkBoard(puck):
                print("Game finished!", puck, "wins!")
                break


    print("Want to play again?  [Enter] YES  [N] NO")
    promptPlayer = ord(msvcrt.getch())
    if promptPlayer == 110 or promptPlayer == 78: 
        print('Thank you for playing!')
        break
    else:
        resetBoard()
        del gameHistory[:] 
        gameHistory = [0]
        nextTurn = 0
