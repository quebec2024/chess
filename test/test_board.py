#lower case for white
#upper case for black 

from chess.board import create_new_board

def test_place():
    board = create_new_board()
    board[2][0] = "K"
    assert board == [["R","H","B","Q","K","B","H","R"],
                    ["P","P","P","P","P","P","P","P"],
                    ["K"," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],        
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],
                    ["p","p","p","p","p","p","p","p"],
                    ["r","h","b","k","q","b","h","r"]]