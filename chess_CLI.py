import chess
import chess.svg
from IPython.display import display,HTML,clear_output
import random

def white(board):
    move = random.choice(list(board.legal_moves))
    return move

def black(board):
    move = None
    PossibleMoves = list(board.legal_moves)
    IsPossible = False
    while move == None or IsPossible == False:
        move = input('Input your move: ')
        move = chess.Move.from_uci(move)
        if move in PossibleMoves: 
            IsPossible = True
    return move
        
def checkWinner(board):
    isGameOver = False
    if board.is_checkmate():
            msg = "Checkmate: "
            result = not board.turn
            isGameOver = True
    elif board.is_stalemate():
        msg = "Draw: stalemate"
        isGameOver = True
    elif board.is_insufficient_material():
        msg = "Draw: insufficient material"
        isGameOver = True
    elif board.can_claim_draw():
        msg = "draw:claim"
        isGameOver = True
    print(msg)

    return(msg,board)

def play_game():
    board = chess.Board()
    while not board.is_game_over(claim_draw=True):
        if board.turn == chess.WHITE:
            move = white(board)
        if board.turn == chess.BLACK:
            move = black(board)
            print(move)
        print(move)
        board.push(move)
        print(board)
        display(chess.svg.board(board))
    checkWinner(board)

play_game()