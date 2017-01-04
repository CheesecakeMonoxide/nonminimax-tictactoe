import sys, random

tictactoeBoard = {'top-L': ' ', 'top-M': ' ', 'top-R' :' ',
                  'mid-L': ' ', 'mid-M': ' ', 'mid-R' :' ',
                  'low-L': ' ', 'low-M': ' ', 'low-R' :' '}

def printBoard(board):
    print ('| ' + board['top-L'] + ' || ' + board['top-M'] + ' || ' + board['top-R'] + ' |')
    print ('---------------')
    print ('| ' + board['mid-L'] + ' || ' + board['mid-M'] + ' || ' + board['mid-R'] + ' |')
    print ('---------------')
    print ('| ' + board['low-L'] + ' || ' + board['low-M'] + ' || ' + board['low-R'] + ' |')

def instruc():
    welcomemsg = ('  Welcome! Try to beat the tictactoe machine if you can!  ')
    print(welcomemsg.center(60, '#'))
    print('')
    print('IMPORTANT INSTRUCTION:')
    print('Take note of the following moves you should type when the game prompts you to input a space.')
    print('')
    print('|top-L||top-M||top-R|')
    print('---------------------')
    print('|mid-L||mid-M||mid-R|')
    print('---------------------')
    print('|low-L||low-M||low-R|')
    print('')
    print('')
    
def spaceIsValid(board, s):
    if s in board.keys():
        return True

def spaceIsFree(board, s):
    if board[s] == ' ':
        return True
    
def winningCombo(board, m, L, M, R):
    if board[L] == m and board[M] == m and board[R] == m:
        return True

def check4WinningCombo(board, m):
    if winningCombo(board, m, 'top-L', 'top-M', 'top-R'):
        return True
    if winningCombo(board, m, 'mid-L', 'mid-M', 'mid-R'):
        return True
    if winningCombo(board, m, 'low-L', 'low-M', 'low-R'):
        return True
    if winningCombo(board, m, 'top-L', 'mid-M', 'low-R'):
        return True
    if winningCombo(board, m, 'top-R', 'mid-M', 'low-L'):
        return True
    if winningCombo(board, m, 'top-L', 'mid-L', 'low-L'):
        return True
    if winningCombo(board, m, 'top-M', 'mid-M', 'low-M'):
        return True
    if winningCombo(board, m, 'top-R', 'mid-M', 'low-R'):
        return True

def computersTurn(board, m):
    for noValueKeys in board.keys():
        if spaceIsFree (board, noValueKeys):
            board[noValueKeys] = m
            if check4WinningCombo(board, m):
                return noValueKeys
            else:
                board[noValueKeys] = ' '
                
    if m == 'X':
            m = 'O'
    else:
        m = 'X'
    for noValueKeys in board.keys():
        if spaceIsFree (board, noValueKeys):
            board[noValueKeys] = m
            if check4WinningCombo(board, m):
                return noValueKeys
            else:
                board[noValueKeys] = ' '

    if m == 'X':
        m = 'O'
    else:
        m = 'X'

    if board['mid-M'] == ' ':
        return 'mid-M'

    elif board['mid-M'] == m:
        if computerTakesEdge(board):
            return computerTakesEdge(board)
        else:
            return computerTakesCorner(board)
    
    elif board['mid-M'] != m:
        if computerTakesCorner(board):
            return computerTakesCorner(board)
        else:
            return computerTakesEdge(board)

def computerTakesEdge(board):
    edges = ['top-M', 'mid-L', 'low-M', 'mid-R']
    random.shuffle(edges)
    for edge in edges:
        if spaceIsFree(board, edge):
            return edge

def computerTakesCorner(board):
    corners = ['top-L', 'top-R', 'low-L', 'low-R']
    random.shuffle(corners)
    for corner in corners:
        if spaceIsFree(board, corner):
            return corner

def turnsMaxedOut(board):
    for noValueKeys in board.keys():
        if spaceIsFree(board, noValueKeys):
            return False
    return True
            
instruc()
printBoard(tictactoeBoard)

print ('Human, pick X or O, or none to end game.')
print ('(X goes first)')

move = input()
move = move.upper()

while True:
    if move == 'X':
        print ('You go first.')
        for turns in range (5):
            move = 'X'
            print ('Pick a space.')
            space = input()
            while True:
                if spaceIsValid(tictactoeBoard, space) and spaceIsFree(tictactoeBoard, space):
                    tictactoeBoard[space] = move
                    printBoard(tictactoeBoard)
                    break
                else:
                    print('Either the space you entered is not valid or it is already taken. See instructions above and pick again.')
                    space = input()
                    continue
            if check4WinningCombo(tictactoeBoard, move):
                print('Human wins the game. Game ends here.')
                sys.exit()
            if turnsMaxedOut(tictactoeBoard):
                print ('Nobody won the game. Game ends here.')
                sys.exit()
            else:
                move = 'O'
                print ('The computer has made its move.')
                space = computersTurn(tictactoeBoard, move)
                tictactoeBoard[space] = move
                printBoard(tictactoeBoard)
                if check4WinningCombo(tictactoeBoard, move):
                    print('The computer wins the game. Game ends here.')
                    sys.exit()
        
    if move == 'O':
        print('The computer will go first.')
        for turns in range (5):
            move = 'X'
            print ('The computer has made its move.')
            space = computersTurn(tictactoeBoard, move)
            tictactoeBoard[space] = move
            printBoard(tictactoeBoard)
            if check4WinningCombo(tictactoeBoard, move):
                    print('The computer wins the game. Game ends here.')
                    sys.exit()
            if turnsMaxedOut(tictactoeBoard):
                print ('Nobody won the game. Game ends here.')
                sys.exit()
            else:
                print('It is now your turn. Pick a space.')
                move = 'O'
                space = input()
                while True:
                    if spaceIsValid(tictactoeBoard, space) and spaceIsFree(tictactoeBoard, space):
                        tictactoeBoard[space] = move
                        printBoard(tictactoeBoard)
                        break
                    else:
                        print('Either the space you entered is not valid or it is already taken. See instructions above and pick again.')
                        continue
                if check4WinningCombo(tictactoeBoard, move):
                    print('The computer wins the game. Game ends here.')
                    sys.exit()           

    if move == '':
        print ('You chose to quit the game.')
        sys.exit()

    else:
        print ('Pick only either X or O.')
        move = input()
        move = move.upper()
        continue
