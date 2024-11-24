#defining board
board = [
    [("r", "b"), ("n", "b"), ("b", "b"), ("q", "b"), ("k", "b"), ("b", "b"), ("n", "b"), ("r", "b")],
    [("p", "b"), ("p", "b"), ("p", "b"), ("p", "b"), ("p", "b"), ("p", "b"), ("p", "b"), ("p", "b")],
    [("", ""), ("", ""), ("", ""), ("", ""), ("k", "w"), ("", ""), ("", ""), ("", "")],
    [("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", "")],
    [("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", "")],
    [("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", "")],
    [("p", "w"), ("p", "w"), ("p", "w"), ("p", "w"), ("p", "w"), ("p", "w"), ("p", "w"), ("p", "w")],
    [("r", "w"), ("n", "w"), ("b", "w"), ("q", "w"), ("", ""), ("b", "w"), ("n", "w"), ("r", "w")]
]
#defining functions
def find_piece_positions(board, piece):
    positions = []
    for row in range(8):
        for col in range(8):
            if board[row][col] == piece:
                positions.append((row, col))
    return positions

def pawn_check(board, verbose=True):
#because of the way pawns attack we dont need to check for a
#king being in check at the opposite end of the board
#and this can help reduce out of range errors
    white_in_check = False
    black_in_check = False

    white_king_pos = find_piece_positions(board, ('k', 'w'))[0]
    black_king_pos = find_piece_positions(board, ('k', 'b'))[0]

    white_king_row, white_king_col = white_king_pos
    black_king_row, black_king_col = black_king_pos

    #checking if white king is in check
    if white_king_row > 0: #to stop out of range errors
        if white_king_col > 0 and board[white_king_row - 1][white_king_col - 1] == ('p', 'b'):
            white_in_check = True
        if white_king_col < 7 and board[white_king_row - 1][white_king_col + 1] == ('p', 'b'):
            white_in_check = True

    #checking if black king is in check
    if black_king_row < 7:#to stop out of range errors
        if black_king_col > 0 and board[black_king_row + 1][black_king_col - 1] == ('p', 'w'):
            black_in_check = True
        if black_king_col < 7 and board[black_king_row + 1][black_king_col + 1] == ('p', 'w'):
            black_in_check = True

    if verbose: #if verbose == True:
        if white_in_check:
            print(f"White king is in check at position {white_king_pos}")
        if black_in_check:
            print(f"Black king is in check at position {black_king_pos}")

    return (white_in_check, black_in_check)

#funcion calling
positions = find_piece_positions(board, ("k", "w"))
print(positions)

result = pawn_check(board, verbose=True)
print(result)
