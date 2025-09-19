"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count , o_count = 0, 0
    for line in board:
        for element in line :
            if element == X :
                x_count += 1
            elif element == O:
                o_count += 1
    
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                actions.append((i,j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    new_board = copy.deepcopy(board)
    filling = player(board)
    i , j = action
    if board[i][j] is not EMPTY:
        raise Exception("unconventional move")
    new_board[i][j] = filling
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY :
            return board[i][0]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for h in board:
        for cell in h:
            if cell == EMPTY:
                return False 
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    v = []
    Actions = actions(board)
    turn = player(board)

    if turn == X :
        for action in Actions:
            v.append(min_value(result(board,action)))
        return Actions[argmax(v)]
    elif turn == O:
        for action in Actions:
            v.append(max_value(result(board,action)))
        return Actions[argmin(v)]
    
    





def argmax(v):
#get the index of the max_value in the list v
    ix = 0
    max = v[0]
    for i, x in enumerate(v):
        if x > max:
            ix, max = i, x 
    return ix


def argmin(v):
    # get the index of the min_value in the list v
    ix = 0 
    min = v[0]
    for i, x in enumerate(v):
        if x < min:
            ix, min = i, x  
    return ix

def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = 2
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -2
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v


    




