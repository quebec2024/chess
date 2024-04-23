from chess.board import create_new_board

def test_move():
    board = create_new_board()
    move([0, 0], [1, 0], board)
    assert board == [[" "," "," "," "," "," "," "," "],
                    ["p"," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],        
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "]]
    
# VERUFY PAN MOVE IS TO TELL IF TI WORKS OR NOT
# true or false
# starting and ending location 
