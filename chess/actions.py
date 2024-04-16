def check ( king , move, location, board):
    print("Check function")

def   check_mate (screen, move , board):
    print("check the mate")

def change_of_character (color, location, board):
    print("change the character")

def castling (movement , board, location):
    print("check castling")
    
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
