
def decidePlayer(turns):
    if turns % 2 == 1:
        return 1
    else:
        return 2
    

def takePlayerInput(player, inputs):

    validInput = False
    while not validInput:

        playerInput = input(f'player {player} turn :')

        if (playerInput.isnumeric() == False or
            int(playerInput) not in range(1,10) or
            playerInput in inputs):
            print('enter valid input!!')
        else:
            return playerInput
    

def checkRows(rows):

    for row in rows:
        if len(set(row)) == 1 and '_' not in row:
            return True
    
    for i in range(3):
        column = []
        for j in range(3):
            column.append(rows[j][i])
        if len(set(column)) == 1 and '_' not in column:
            return True 
        
    if ((rows[0][0] == rows[1][1] == rows[2][2] and rows[1][1] != '_') or
       (rows[0][2] == rows[1][1] == rows[2][0] and rows[1][1] != '_')):
        return True     
        

def arrangeRows(rows, player, symbols, playerInput):
    if playerInput in range(1,4):
        rows[0][playerInput-1] = symbols[player-1]
    elif playerInput in range(4,7):
        rows[1][playerInput-4] = symbols[player-1]
    elif playerInput in range(7,10):
        rows[2][playerInput-7] = symbols[player-1]
    

def printRows(rows):
    for row in rows:
        print(row)


def selectSymbol():

    validSymbols = False
    while not validSymbols:
        player1 = input('player 1 choose symbol : ')
        player2 = input('player 2 choose symbol : ')
        if len(set([player1, player2])) == 1:
            print('enter different symbols!!')
        else:
            return [player1, player2]

def result(winner, player, turns):

    if winner:
        printRows(rows)
        print(f'player {player} won!!')
        nextGame = input('Next Game???')
        if nextGame in ['y', 'Y']:
            return False
        else:
            return True
        
    if turns == 9:
        printRows(rows)
        print('game draw!!')
        nextGame = input('Next Game???')
        if nextGame in ['y', 'Y']:
            return False
        else:
            return True
        

def playGame():

    symbols = selectSymbol()
    inputs = []

    for turns in range(1,10):
        
        printRows(rows)

        player = decidePlayer(turns)  

        playerInput = takePlayerInput(player, inputs)
        inputs.append(playerInput)

        arrangeRows(rows, player, symbols, int(playerInput))

        winner = checkRows(rows)

        gameover = result(winner, player, turns)

        if winner  or turns == 9:
            return gameover

stoptheGame = False
while not stoptheGame:
    row1 = ['_','_','_']
    row2 = ['_','_','_']
    row3 = ['_','_','_']
    rows = [row1, row2, row3]

    stoptheGame = playGame()


    

