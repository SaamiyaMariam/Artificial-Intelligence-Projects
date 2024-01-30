# Create a 2D list to represent the chessboard
ch_board = [
              ['BR','BT','BB','BQ','BK','BB','BT','BR'],
              ['BP','BP','BP','BP','BP','BP','BP','BP'],
              ['  ','  ','  ','  ','  ','  ','  ','  '],
              ['  ','  ','  ','  ','  ','  ','  ','  '],
              ['  ','  ','  ','  ','  ','  ','  ','  '],
              ['  ','  ','  ','  ','  ','  ','  ','  '],
              ['WP','WP','WP','WP','WP','WP','WP','WP'],
              ['WR','WT','WB','WQ','WK','WB','WT','WR']]

def drawBoard(board):
    print('  +---------------------------------------+')
    for row in range(len(board)):
        ch = str(row) + ' |'
        print(ch , end=' ')
        for c in range(len(board[row])):
            if board[row][c] == '  ':
                print("  ", end=' | ')
            else:
                print(board[row][c], end=' | ')
        print('')
        print('-------------------------------------------')
    
    print('    0    1    2    3    4    5    6    7 ')    

def get_queen_moves(index, board):
    possible_moves = []
    row, colm = index #index is a 2d tuple holding the position of the queen on the board

    # possible moves that can be made vertically and horizontally
    for i in range(8):
        # if this row != current column, queen can move in it horizontally
        if i != colm:
            # if this certain square is empty or occupied by a piece of the opp colour, the queen can move here
            if board[row][i] == '  ' or ( board[row][colm][0] != board[row][i][0]):
                # adding this square to the list of possible moves
                possible_moves.append((row,i))
        # if this row != current row, queen can move in it vertically
        if i != row:
            # if this certain square is empty or occupied by a piece of the opp colour, the queen can move here
            if board[i][colm] == '  ' or ( board[row][colm][0] != board[i][colm][0]):
                # adding this sqaure to the list of possible moves
                possible_moves.append((i, colm))

    # possible moves that the Queen can make diagonally
    # the queen can move diagonally if the squares are empty or piece of opp color is on the square (if it is encountered, the queen cannot proceed further)
    high = 8
    low = 1

    # forward diagonal, to the right
    for i in range(low,high):
        # disqualify invalid indexes
        if (colm + i) > 7 or (row + i) > 7:
            break
        # in case the square is empty, move is valid
        if board[row + i][colm + i] == '  ':
            possible_moves.append((row+i, colm+i))
        # in case the square has a piece of the opossite color, we can add it to our list of possible moves
        elif board[row+i][colm+i][0] != board[row][colm][0]:
            possible_moves.append((row+i,colm+i))
            break # the queen cannot move beyond this point so we break the loop
        else:
            break

    # backward diagonal, to the left
    for i in range(low,high):
        # disqualify invalid indexes
        if (colm - i) < 0 or (row - i) < 0:
            break
        # in case the square is empty, move is valid
        if board[row-i][colm -i] == '  ':
            possible_moves.append((row-i,colm-i))
        # in case the square has a piece of the opossite color, we can add it to our list of possible moves
        elif board[row-i][colm-i][0] != board[row][colm][0]:
            possible_moves.append((row-i,colm-i))
            break # the queen cannot move beyond this point so we break the loop
        else:
            break

    # forward diagonal, to the left
    for i in range(low,high):
        # disqualify invalid indexes
        if (row + i) > 7 or (colm - i) < 0:
            break
        # in case the square is empty, move is valid
        if board[row+i][colm -i] == '  ':
            possible_moves.append((row+i,colm-i))
        # in case the square has a piece of the opossite color, we can add it to our list of possible moves
        elif board[row+i][colm-i][0] != board[row][colm][0]:
            possible_moves.append((row+i,colm-i))
            break # the queen cannot move beyond this point so we break the loop
        else:
            break

    # backward diagonal, to the right
    for i in range(low,high):
        # disqualify invalid indexes
        if (colm + i) > 7 or (row - i) < 0:
            break
        # in case the square is empty, move is valid
        if board[row-i][colm +i] == '  ':
            possible_moves.append((row-i,colm+i))
        # in case the square has a piece of the opossite color, we can add it to our list of possible moves
        elif board[row-i][colm+i][0] != board[row][colm][0]:
            possible_moves.append((row-i,colm+i))
            break # the queen cannot move beyond this point so we break the loop
        else:
            break

    return possible_moves

def get_rook_moves(index, board):
    # rook can move horizontally and vertically if path is unblocked
    row, colm = index 
    possible_moves = []

    # possible moves that can be made vertically and horizontally
    for i in range(8):
        # if this row != current column, rook can move in it horizontally
        if i != colm:
            # if this certain square is empty or occupied by a piece of the opp colour, the rook can move here
            if board[row][i] == '  ' or ( board[row][colm][0] != board[row][i][0]):
                # adding this square to the list of possible moves
                possible_moves.append((row,i))
        # if this row != current row, rook can move in it vertically
        if i != row:
            # if this certain square is empty or occupied by a piece of the opp colour, the rook can move here
            if board[i][colm] == '  ' or ( board[row][colm][0] != board[i][colm][0]):
                # adding this sqaure to the list of possible moves
                possible_moves.append((i, colm))

    return possible_moves

def get_bishop_moves(index, board):
    row, colm = index
    # since the bishop can only move within squares of the colour it currently stands on, so we must check that color
    curr_color = (row + colm) % 2
    # 0: white, 1: black

    possible_moves = []

    high = 8
    low = 1

    # forward diagonal, to the right
    for i in range(low,high):
        # disqualify invalid indexes
        if (colm + i) > 7 or (row + i) > 7:
            break
        
        # checking square colors
        if (curr_color ==  ((colm + i) + (row + i) % 2)):
            # in case the square is empty, move is valid
            if board[row + i][colm + i] == '  ':
                possible_moves.append((row+i,colm+i))
            # in case the square has a piece of the opossite color, we can add it to our list of possible moves
            elif board[row+i][colm+i][0] != board[row][colm][0]:
                possible_moves.append((row+i,colm+i))
                break # the bishop cannot move beyond this point so we break the loop
            else:
                break

    # backward diagonal, to the left
    for i in range(low,high):
        # disqualify invalid indexes
        if (colm - i) < 0 or (row - i) < 0:
            break
        # checking square colors
        if (curr_color ==  ((colm - i) + (row - i) % 2)):
            # in case the square is empty, move is valid
            if board[row-i][colm -i] == '  ':
                possible_moves.append((row-i,colm-i))
            # in case the square has a piece of the opossite color, we can add it to our list of possible moves
            elif board[row-i][colm-i][0] != board[row][colm][0]:
                possible_moves.append((row-i,colm-i))
                break # the bishop cannot move beyond this point so we break the loop
            else:
                break

    # forward diagonal, to the left
    for i in range(low,high):
        # disqualify invalid indexes
        if (row + i) > 7 or (colm - i) < 0:
            break
        # checking square colors
        if (curr_color ==  ((colm + i) + (row - i) % 2)):

            # in case the square is empty, move is valid
            if board[row+i][colm -i] == '  ':
                possible_moves.append((row+i,colm-i))
            # in case the square has a piece of the opossite color, we can add it to our list of possible moves
            elif board[row+i][colm-i][0] != board[row][colm][0]:
                possible_moves.append((row+i,colm-i))
                break # the bishop cannot move beyond this point so we break the loop
            else:
                break

    # backward diagonal, to the right
    for i in range(low,high):
        # disqualify invalid indexes
        if (colm + i) > 7 or (row - i) < 0:
            break
        # checking square colors
        if (curr_color ==  ((colm + i) + (row - i) % 2)):

            # in case the square is empty, move is valid
            if board[row-i][colm +i] == '  ':
                possible_moves.append((row-i,colm+i))
            # in case the square has a piece of the opossite color, we can add it to our list of possible moves
            elif board[row-i][colm+i][0] != board[row][colm][0]:
                possible_moves.append((row-i, colm+i))
                break # the bishop cannot move beyond this point so we break the loop
            else:
                break

    return possible_moves   

def get_knight_moves(index, board):
    row, colm = index
    possible_moves = []

    # moves two squares horizontally or vertically and then makes a right-angle turn for one more square
    possible_offsets = [
        (-1,-2), (-1,2), (1,-2), (1,2), #2 sqrs vertical
        (-2,-1), (-2,1), (2,-1), (2,1) #2 sqrs horizontal
    ]

    for i, j in possible_offsets:
        r = row + i
        c = colm + j
        if( (r>=0 and r<8) and (c>=0 and c<8)):
            possible_moves.append((r,c))

    return possible_moves

def get_king_moves(index, board):
    row,colm = index
    possible_moves = []

    possible_offsets = [
        (-1,0), (1,0), #left and right
        (0,1), (0,-1), #up and down
        (1,1), (1,-1), (-1,1), (-1,-1) #diagonals
    ]

    for i,j in possible_offsets:
        r = i + row
        c = j + colm
        if (r>=0 and r<8) and (c>=0 and c<8): #checking whether in bounds
            possible_moves.append((r,c))

    return possible_moves

def get_pawn_moves(index, board):
    row,colm = index
    possible_moves = []

    black_offset = 1
    white_offset = -1

    if(board[row][colm][0] == 'W'):
        offset = white_offset
    elif(board[row][colm][0] == 'B'):
        offset = black_offset

    # if pawn can move one square forward
    if board[row + offset][colm] == '  ':
        possible_moves.append((row+offset, colm))

        # check if this was the pawn's first move
        if (board[row][colm][0] == 'W' and row == 6) or (board[row][colm][0] == 'B' and row == 1):
            # check if it can move another square forward
             if board[row + (2*offset)][colm] == '  ':
                possible_moves.append((row+(2*offset), colm))

    # possible diagonal moves for pawn
    # diagonally to the left
    if colm > 0:
        # if color is not same and square is not empty, we can move diagonally
        if board[row][colm][0]!= board[row+offset][colm-1] and board[row+offset][colm-1] != '  ':
            possible_moves.append((row+offset, colm-1))
    # diagonally to the right
    if colm < 7:
        # if color is not same and square is not empty, we can move diagonally
        if board[row][colm][0]!= board[row+offset][colm+1] and board[row+offset][colm+1] != '  ':
            possible_moves.append((row+offset, colm+1))

    return possible_moves            

def ret_king_index(color, board):
    # iterate board until we find king of specified team
    for i in range(8):
        for j in range(8):
            if(board[i][j][0] == color and board[i][j][1]=='K'):
                return ((i,j))
    return '  ' #if not found

def moves_of_opp(team, board):

    opp_moves = []
    if team == 'W':
        opp = 'B'
    else:
        opp = 'W'
    
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            # if piece is off opp color and exists
            if piece[0] == opp and piece != '  ':
                # check what kind of piece it is
                if piece[1] == 'Q':
                    moves = get_queen_moves((i,j),board)
                if piece[1] == 'K':
                    moves = get_king_moves((i,j),board) 
                if piece[1] == 'T':
                    moves = get_knight_moves((i,j),board)
                if piece[1] == 'B':
                    moves = get_bishop_moves((i,j),board)
                if piece[1] == 'P':
                    moves = get_pawn_moves((i,j),board)
                if piece[1] == 'R':
                    moves = get_rook_moves((i,j),board)
                
                opp_moves.extend(moves)
    return opp_moves

def get_piece_moves(piece_pos, board):

    i,j = piece_pos
    piece = board[i][j]
    if piece != '  ':
            # check what kind of piece it is
            if piece[1] == 'Q':
                moves = get_queen_moves((i,j), board)
            if piece[1] == 'K':
                moves = get_king_moves((i,j), board) 
            if piece[1] == 'T':
                moves = get_knight_moves((i,j), board)
            if piece[1] == 'B':
                moves = get_bishop_moves((i,j), board)
            if piece[1] == 'P':
                moves = get_pawn_moves((i,j), board)
            if piece[1] == 'R':
                moves = get_rook_moves((i,j), board)
    return moves

def Check(color, board):

    king_index = ret_king_index(color, board)
    k_row, k_col = king_index
    in_check = False
    
    for i in range(len(board)): #chekcig each row in the board
        for j in range(len(board[i])): #checking each square in the row

            if board[i][j][0]!= color and board[i][j] != '  ': #piece is opp and not empty
                # if sq and king have the same index, king is in check
                if king_index in get_piece_moves((i,j), board):
                    in_check = True
    return in_check

# def CheckMate(color):

#     king_pos = ret_king_index(color)
#     moves_king = get_king_moves(king_pos)

#     # if not in check, then automatically not in checkmate
#     if Check(color) == False:
#         return False
    
#     # if in check, me must see if we can remove king from this position
#     for i in moves_king:
#         # get enemy moves
#         opp_moves = moves_of_opp(color)

def move_piece(start_pos, end_pos, board):

    s_r, s_c = start_pos
    e_r, e_c = end_pos
    

    mov = get_piece_moves(start_pos, board)
    
    if end_pos not in mov:
        print("This move is invalid!")
        return False
    
    # updating board
    board[e_r] [e_c] = board[s_r] [s_c]
    board[s_r] [s_c] = '  '
    return True

def evaluate_board(board):
    # A simple evaluation function that returns 1 if white is in check, -1 if black is in check, and 0 otherwise.
    if Check('W', board):
        return 1
    elif Check('B', board):
        return -1
    else:
        return 0

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or Check('W', board) or Check('B', board):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in generate_moves(board, 'W'):
            new_board = make_move(board, move)
            eval = minimax(new_board, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for move in generate_moves(board, 'B'):
            new_board = make_move(board, move)
            eval = minimax(new_board, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

def generate_moves(board, color):
    # Function to generate all possible moves for a given color
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j][0] == color:
                piece_moves = get_piece_moves((i, j), board)
                for move in piece_moves:
                    moves.append(((i, j), move))
    return moves

def make_move(board, move):
    # Function to make a move on the board and return the new board
    start_pos, end_pos = move
    s_r, s_c = start_pos
    e_r, e_c = end_pos
    new_board = [row[:] for row in board]  # Create a copy of the board
    new_board[e_r][e_c] = new_board[s_r][s_c]
    new_board[s_r][s_c] = '  '
    return new_board

def best_move(board, depth, maximizing_player):
    best_score = float('-inf') if maximizing_player else float('inf')
    best_move = None
    color = 'W' if maximizing_player else 'B'
    moves = generate_moves(board, color)
    
    for move in moves:
        new_board = make_move(board, move)
        score = minimax(new_board, depth - 1, not maximizing_player, float('-inf'), float('inf'))
        
        if maximizing_player and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing_player and score < best_score:
            best_score = score
            best_move = move
    
    return best_move

if __name__ == "__main__" :
    # Drawing  chessboard on terminal
    drawBoard(ch_board)

    pos = (0,3)
    mov = get_queen_moves(pos, ch_board)
    print(mov)
    print("")
    if move_piece((0,3), (4,3), ch_board) == True:
        drawBoard(ch_board)

    print("Is White Team In Check? ", Check('W', ch_board))
