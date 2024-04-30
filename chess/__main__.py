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
        move(start,end, board)
    elif command == "castling":
        castling()
    elif command == "q":
        exit()
    else:
        print("I did not understand this command.")
        


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

