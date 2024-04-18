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

while TRUE:
    print_board(board)

def create_new_board():
    board = [[" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],        
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]]
    return board
   
def print_board(board):
     print(
         f"""
            {board[0][0]}|{board[0][1]}|{board[0][2]}|{board[0][3]}|{board[0][4]}|{board[0][5]}|{board[0][6]}|{board[0][7]}
            {board[1][0]}|{board[1][1]}|{board[1][]}|{board[1][3]}|{board[1][4]}|{board[1][5]}|{board[1][6]}|{board[1][7]}
            {board[2][0]}|{board[2][1]}|{board[2][]}|{board[2][3]}|{board[2][4]}|{board[2][5]}|{board[2][6]}|{board[2][7]}
            {board[3][0]}|{board[3][1]}|{board[3][]}|{board[3][3]}|{board[3][4]}|{board[3][5]}|{board[3][6]}|{board[3][7]}
            {board[4][0]}|{board[4][1]}|{board[4][]}|{board[4][3]}|{board[4][4]}|{board[4][5]}|{board[4][6]}|{board[4][7]}
            {board[5][0]}|{board[5][1]}|{board[5][]}|{board[5][3]}|{board[5][4]}|{board[5][5]}|{board[5][6]}|{board[5][7]}
            {board[6][0]}|{board[6][1]}|{board[6][]}|{board[6][3]}|{board[6][4]}|{board[6][5]}|{board[6][6]}|{board[6][7]}
            {board[7][0]}|{board[7][1]}|{board[7][]}|{board[7][3]}|{board[7][4]}|{board[7][5]}|{board[7][6]}|{board[7][7]}
"""
     )

def reset_board(board):
    print