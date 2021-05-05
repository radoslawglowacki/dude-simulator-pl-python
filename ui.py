def display_board(board):
    for line in board:
        string_representation = ""
        for elm in line:
            string_representation += elm
        print(string_representation)
