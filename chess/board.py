def pawns (color,locaation,board,move, Move forward one square, but capture diagonally. On their first move, they can move forward two squares.):
    pass 
def bishops (color,locaation,board,move, Move diagonally across any number of squares.):
    pass
def knights (color,locaation,board,move, Move in an "L" shape: two squares in one direction and then one square perpendicular, or one square in one direction and then two squares perpendicular. They can jump over other pieces.):
    pass
def rooks (color,locaation,board,move, Move in a straight line horizontally or vertically across any number of squares.):
    pass
def queen (color,locaation,board,move, Combine the power of the rook and bishop, moving horizontally, vertically, or diagonally across any number of squares.):
    pass
def king (color,locaation,board,move,  Move one square in any direction. The king can also perform a special move called castling, where the king and a rook are allowed to move at the same time.):
    pass

#borad setup
#Place the board between the two players. Each player should have a white (or light-colored) square at the bottom-right corner.
#Arrange the pieces on the two rows closest to each player. The second row from each player is filled with pawns.
#The first row, from left to right, should be arranged as: Rook, Knight, Bishop, Queen, King, Bishop, Knight, and Rook. Remember, the queen goes on her own matching color (white queen on white, black queen on black).


def create_new_board():
    board = ((" "," "," "," "," "," "," "," ")),
            ((" "," "," "," "," "," "," "," ")),
            ((" "," "," "," "," "," "," "," ")),
            ((" "," "," "," "," "," "," "," ")),        
            ((" "," "," "," "," "," "," "," ")),
            ((" "," "," "," "," "," "," "," ")),
            ((" "," "," "," "," "," "," "," ")),
            ((" "," "," "," "," "," "," "," "))
    
def print_board(board):
     print(
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
            (("board()()","board()()","board()()","board()()","board()()","board()()","board()()","board()()")),
     )
