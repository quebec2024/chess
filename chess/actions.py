def verify_check (board):
    print("Check function")

def verify_check_mate (board):
    print("check the mate")

def verify_change_of_piece(board):
    pass

def change_of_piece(new_piece, location, board):
    print("change the character")

def castling(movement, board, location):
    print("check castling")

def move(start, end, board):
    start_row = start[0]
    start_col = start[1]
    end_row = end[0]
    end_col = end[1]
    board[end_row][end_col] = board[start_row][start_col]
    print("`Moving a piece")
    
# board[end_row[0]][end_col[0]] = board[start_row[0]][start_col[0]]

def verify_pawn_move(color,locaation,board,move,):
    print ("Move forward one square, but capture diagonally. On their first move, they can move forward two squares.")

def verify_bishop_move(color,locaation,board,move,):
    print ("Move diagonally across any number of squares")

def veryfy_knights_move(color,locaation,board,move):
    print ("Move in an 'L' shape: two squares in one direction and then one square perpendicular. They jump over other pieces")

def verify_rook_move(color,locaation,board,move):
    print("Move in a straight line horizontally or vertically across any number of squares")

def verify_queen_move(color,locaation,board,move): 
    print ("Combine the power of the rook and bishop, moving horizontally, vertically, or diagonally across any number of squares")

def verify_king_move(color,locaation,board,move): 
    print ("Move one square in any direction. The king can also perform a special move called castling, where the king and a rook are allowed to move at the same time")

# if check=True
#     print ("move your king")
#     elif print ("its your turn")

# if check_mate=True
#     print ("you lose the match")
#     elif print ("defend your area")

# if check=True
#     print("change to queen")
#     elif print ("use queen moves , diagonal")
# if check=True
#     print ("the king moves two squares foward")
#     elif print ("tower moves to the otrher side of the king")

# if check=True
#     print ("pawn moves forward")
#     elif print ("")

# if move[0] == 1 and color == "white":
#         print("Move forward")
#     elif move[0] == -1 and color == "black":
#         print("Move forward")

# if verify_bishop_move=True 
#     print ("You are moving your bishop")
#     elif print ("diagonal moves")

# if veryfy_knights_move=True
#     print("move one knight")
#     elif print ("L moves")

# if verify_rook_move=True
#     print (" displacemente of rook")
#     elif print("x movements")
    
    
