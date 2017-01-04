# FIX BUG ALLAN FOUND - COMPUTER WON EVEN THOUGH HUMAN WON (DOUBLE BIND)


import sys, random, time

tictactoeBoard = {'1': ' ', '2': ' ', '3' :' ',
                  '4': ' ', '5': ' ', '6' :' ',
                  '7': ' ', '8': ' ', '9' :' '}

def printBoard(board):
    print ('| ' + board['1'] + ' || ' + board['2'] + ' || ' + board['3'] + ' |')
    print ('---------------')
    print ('| ' + board['4'] + ' || ' + board['5'] + ' || ' + board['6'] + ' |')
    print ('---------------')
    print ('| ' + board['7'] + ' || ' + board['8'] + ' || ' + board['9'] + ' |')

def instruc():
    welcomemsg = ('  Welcome! Try to beat the tictactoe machine if you can!  ')
    print(welcomemsg.center(60, '#'))
    print('')
    print('IMPORTANT INSTRUCTION:')
    print('Take note of the following moves you should type when the game prompts you to input a space.')
    print('')
    print('| 1 || 2 || 3 |')
    print('---------------')
    print('| 4 || 5 || 6 |')
    print('---------------')
    print('| 7 || 8 || 9 |')
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
    if winningCombo(board, m, '1', '2', '3'):
        return True
    if winningCombo(board, m, '4', '5', '6'):
        return True
    if winningCombo(board, m, '7', '8', '9'):
        return True
    if winningCombo(board, m, '1', '5', '9'):
        return True
    if winningCombo(board, m, '3', '5', '7'):
        return True
    if winningCombo(board, m, '1', '4', '7'):
        return True
    if winningCombo(board, m, '2', '5', '8'):
        return True
    if winningCombo(board, m, '3', '6', '9'):
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

    if board['5'] == ' ':
        return '5'

    elif board['5'] == m:
        if computerTakesEdge(board):
            return computerTakesEdge(board)
        else:
            return computerTakesCorner(board)
    
    elif board['5'] != m:
        if computerTakesCorner(board):
            return computerTakesCorner(board)
        else:
            return computerTakesEdge(board)

def computerTakesEdge(board):
    edges = ['2', '4', '6', '8']
    random.shuffle(edges)
    for edge in edges:
        if spaceIsFree(board, edge):
            return edge

def computerTakesCorner(board):
    corners = ['1', '3', '7', '9']
    random.shuffle(corners)
    for corner in corners:
        if spaceIsFree(board, corner):
            return corner

def turnsMaxedOut(board):
    for noValueKeys in board.keys():
        if spaceIsFree(board, noValueKeys):
            return False
    return True

def playTheGame():
    
    instruc()
    for k in tictactoeBoard.keys():
        tictactoeBoard[k] = ' '
        
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
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        if playAgain == 'N':
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
                if turnsMaxedOut(tictactoeBoard):
                    print ('Nobody won the game. Game ends here.')
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        if playAgain == 'N':
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
                else:
                    move = 'O'
                    print ('The computer has made its move.')
                    space = computersTurn(tictactoeBoard, move)
                    tictactoeBoard[space] = move
                    printBoard(tictactoeBoard)
                    if check4WinningCombo(tictactoeBoard, move):
                        print('The computer wins the game. Game ends here.')
                        print('Do you want to play again? Y/N')
                        playAgain = input()
                        playAgain = playAgain.upper()
                        while True:
                            if playAgain == 'Y':
                                playTheGame()
                            if playAgain == 'N':
                                time.sleep(5)
                                sys.exit()
                            else:
                                print('Type only either Y for yes and N for no.')
                                playAgain = input()
                                playAgain = playAgain.upper()
            
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
                        print('Do you want to play again? Y/N')
                        playAgain = input()
                        playAgain = playAgain.upper()
                        while True:
                            if playAgain == 'Y':
                                playTheGame()
                            if playAgain == 'N':
                                time.sleep(5)
                                sys.exit()
                            else:
                                print('Type only either Y for yes and N for no.')
                                playAgain = input()
                                playAgain = playAgain.upper()
                if turnsMaxedOut(tictactoeBoard):
                    print ('Nobody won the game. Game ends here.')
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        if playAgain == 'N':
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
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
                        print('Human wins the game. Game ends here.')
                        print('Do you want to play again? Y/N')
                        playAgain = input()
                        playAgain = playAgain.upper()
                        while True:
                            if playAgain == 'Y':
                                playTheGame()
                            if playAgain == 'N':
                                time.sleep(5)
                                sys.exit()
                            else:
                                print('Type only either Y for yes and N for no.')
                                playAgain = input()
                                playAgain = playAgain.upper()           

        if move == '':
            print ('You chose to quit the game.')
            time.sleep(3)
            sys.exit()

        else:
            print ('Pick only either X or O.')
            move = input()
            move = move.upper()
            continue

playTheGame()
