# Chess Python Project

## Overview
This Python project implements a simple chess game. The chessboard is represented as a 2D list, and the game supports basic moves for each piece, including pawns, rooks, knights, bishops, queens, and kings.

## Usage
1. The chessboard is initialized with the starting position of pieces.
2. The `drawBoard` function is used to display the current state of the chessboard.
3. Various functions (`get_queen_moves`, `get_rook_moves`, `get_bishop_moves`, `get_knight_moves`, `get_king_moves`, `get_pawn_moves`) are defined to calculate possible moves for each type of chess piece.
4. The `move_piece` function is implemented to make a move on the chessboard.
5. The `Check` function checks whether a given team is in check.
6. The `evaluate_board` function provides a simple evaluation of the board, returning 1 if white is in check, -1 if black is in check, and 0 otherwise.
7. The `minimax` algorithm is implemented for a basic AI to find the best move considering a specified depth.
8. The `generate_moves` and `make_move` functions assist in finding possible moves and making moves on the board.
9. The `best_move` function is used to find the best move for the AI.

## Sample Usage
```python
# Drawing chessboard on terminal
drawBoard(ch_board)

# Getting possible moves for the queen at position (0,3)
pos = (0, 3)
mov = get_queen_moves(pos, ch_board)
print(mov)

# Moving a piece (for example, moving the queen from (0,3) to (4,3))
if move_piece((0, 3), (4, 3), ch_board):
    drawBoard(ch_board)

# Checking if the White team is in check
print("Is White Team In Check? ", Check('W', ch_board))
```

