from board import create_new_board
from board.py import pawns 
from actions.py import check,check_mate,change_of_character,verify_pawn_move,verify_bishop_move,veryfy_knights_move,verify_rook_move,verify_queen_move,verify_king_move

def check():
    board,veryfication = create_new_board()
    [0,7][1,6] = king_check

def check_mate():
    board_verification = verify_king_move()
[0,2][2,0][5,5] = end_game

# test fot the check mate, and when it happens, the game ends. 

def change_of_character():
   board , verification = create_new_board()
   board[0,3] = queen 

   new_board, verification = create_new_board()
   new_board[0,3] = queen
   assert board == new_board

def test_verify_pawn_move():
    is_valid = verify_pawn_move([1,2],[1,3])
    assert is_valid == True

#this test verifies if the piece you want to move, actually moves when you type in the row and colum, so the start and ending position. 
#This action is for the pawn, but there one for each peice of the game. 

def verify_pawn_move():
    print(next_move)
    board, verification = create_new_board
    currrent_colum = move (board)
    assert currrent_colum == 1

def verify_bishop_move():
    print(next_move)
    board, verification = create_new_board
    current_colum = move (board)
    assert current_colum == 2

def verify_knights_move():
    print(next_move)
    board, verification = create_new_board
    current_colum = move (board)
    assert current_colum == 1

def verify_rook_move():
    print(next_move)
    board, verification = create_new_board
    current_colum = move (board)
    assert current_colum == 0

def verify_queen_move():
    print(next_move)
    board, verification = create_new_board
    current_colum = move (board)
    assert current_colum == 3

def verify_king_move():
    print(next_move) 
    board, verification = create_new_board
    current_colum = move (board)
    assert current_colum == 4



