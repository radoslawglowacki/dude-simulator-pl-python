from shutil import copyfile


def create_board(width, height):
    game_board = []
    border_lines = 2
    border_characters = 2

    first_row = []
    first_row.append(" ")
    for _ in range(width):
        first_row.append("_")
    game_board.append(first_row)

    for _ in range(height-border_lines):
        middle_row = []
        middle_row.append("| ")
        for _ in range(width-border_characters):
            middle_row.append(" ")
        middle_row.append(" |")
        game_board.append(middle_row)

    last_row = []
    last_row.append("|")
    for _ in range(width):
        last_row.append("_")
    last_row.append("|")
    game_board.append(last_row)

    return game_board


def put_player_on_board(board, player):
    board[player.get("player_y")][player.get(
        "player_x")] = player.get("player_icon")


def write_map(blank_board, board_width, board_height, file_name, start_row, start_column):
    actual_board = blank_board
    loaded_board_from_file = []

    with open(file_name, 'r') as file:
        for line in file:
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            loaded_board_from_file.append(row)
        j = 0
        for line in loaded_board_from_file:
            i = 0
            for elm in line:
                actual_board[start_row + j][start_column + i] = elm
                i += 1
            j += 1

    return actual_board


def preparing_maps():
    copyfile("art/mapV1.txt", "tmp/mapV1.txt")
    copyfile("art/mapV2.txt", "tmp/mapV2.txt")
    copyfile("art/mapV3.txt", "tmp/mapV3.txt")


def put_drunkard(COPIED_MAP_LOCATION, MAP_PLACING_Y, MAP_PLACING_X, player):
    read_map = []
    with open(COPIED_MAP_LOCATION, 'r+') as f:
        for line in f:
            row = []
            for char in line:
                row.append(char)
            read_map.append(row)
    read_map[(player["player_y"]) -
             MAP_PLACING_Y + 4][(player["player_x"])-MAP_PLACING_X + 3] = "M"
    with open(COPIED_MAP_LOCATION, 'w+') as f:
        for line in read_map:
            str_line = ""
            for char in line:
                str_line += char
            f.write(str_line)


def change_field(COPIED_MAP_LOCATION, MAP_PLACING_Y, MAP_PLACING_X, player, CHAR):
    read_map = []
    with open(COPIED_MAP_LOCATION, 'r+') as f:
        for line in f:
            row = []
            for char in line:
                row.append(char)
            read_map.append(row)
    read_map[(player["player_y"]) -
             MAP_PLACING_Y][(player["player_x"])-MAP_PLACING_X] = CHAR
    with open(COPIED_MAP_LOCATION, 'w+') as f:
        for line in read_map:
            str_line = ""
            for char in line:
                str_line += char
            f.write(str_line)