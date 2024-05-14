from actions import (
    move, verify_bishop_move, verify_rook_move, verify_change_of_piece, verify_check,
    verify_check_mate, verify_king_move, verify_pawn_move, verify_queen_move, veryfy_knights_move,
    castling, change_of_piece,
)
from board import create_new_board, print_board

with open ("README.md", "r" ) as f:
    print(f.read())


board = create_new_board()
while True:
    print_board(board)
    command = input("Enter a command:")
    if command == "move":
        start = input("Starting position:")
        end = input("Ending position:")
        start = [int(start[0]), int(start[1])]
        end = [int(end[0]), int(end[1])]
        move(start,end, board)
    elif command == "castling":
        castling()
    elif command == "q":
        exit()
    else:
        print("I did not understand this command.")
        
#this action is the action that allows you to play the game, it puts the board on the terminal, ands allows you to enter the move action and allows you to tell the game the starting and eniding position of the piece you want to move. 

#instructions
#rules
#Castling: This move involves the king and either rook. It’s performed under certain conditions to help protect the king and connect the rooks.
#En Passant: A special pawn capture that can occur immediately after an opponent moves a pawn two squares forward from its starting position, and another pawn could have captured it had it moved only one square forward.
#Promotion: When a pawn reaches the farthest row from its starting position, it can be promoted to any other piece, typically a queen.

#opening strategy
#Control the center: Try to control the center of the board with your pieces and pawns.
#Develop your pieces: Move your knights and bishops towards the center to be used effectively.
#Keep your king safe: Often, this means castling to protect your king by moving it to a safer position shielded by pawns.

#check and checkmate
#Check: This is a threat to capture the king. The player whose king is in check must make a move that results in the king no longer being in check.
#Checkmate: This occurs when a king is placed in check and there is no legal move to escape check.

#ending the game
#Besides checkmate, a game can end in a draw. Common ways to draw include stalemate (the player to move is not in check but has no legal move), agreement between players, or insufficient material (neither player has enough pieces to force a checkmate).

#Instructions 
#First click the play bottom to start the game and enter the terminal.
#Then enter move in the terminal
#Click on starting position and decide a piece that you want to move then put the position where your piece  is located ( remember that you only need to put the row and then the column without space or commas ex:11 *also remeber that when counting the rows and columns the firt of each one is 0 not 1, so you start counting from 0 ) 
#Then click on ending position and enter the position where you want to move your piece

