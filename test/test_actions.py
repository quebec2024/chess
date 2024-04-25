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

def test_verify_pawn_move():
    if verify_pawn_move([1, 2], [1, 3]):
        print("True, test passed")
    else:
        print("False, test not passed")
    
def test_verify_pawn_move(starting_position, ending_position):


def test_change_of_piece(current_piece, new_piece):
    if chanage_of_piece ("current_piece", "new_piece") == "new_piece":
        print("True, test passed")
    else:
         print("False, test not passed")


def test_verify_check():
    if verify_check("white") == False:
        print("True, test passed")
    else
        print("False, test not passed")
    
    if verify_check("black") == True:
        print("True, test passed")
    else
        print("False, test not passed")


def test_verify_check_mate():
    if verify_check_mate("white") == False:
        print("True, test passed")
    else
        print("False, test not passed")
    
    if verify_check_mate("black") == True:
        print("True, test passed")
    else
        print("False, test not passed")