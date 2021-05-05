import util
import engine
import ui
import time
import msvcrt as m
import winsound
import characters
import boss_scene
import intro_outro
import stats_scores

PLAYER_ICON = 'R'
PLAYER_START_X = 50
PLAYER_START_Y = 15
NOT_ALLOWED = ['[', "]", "_", "|", "/", "\\" "(", ")", "~", "{", "}"]
BOARD_WIDTH = 194
BOARD_HEIGHT = 44
MAP_NAME = "tmp/mapV1.txt"
COPIED_MAP_LOCATION = ""
LOGO_NAME = ""
PLAYER_TYPE = "art/ziomek_banan.txt"
MAP_PLACING_Y = 6
MAP_PLACING_X = 37
IS_RUNNING = True
WIN = 1
PERM = 0


def create_player():
    player = {
        "player_icon": PLAYER_ICON,
        "player_x": PLAYER_START_X,
        "player_y": PLAYER_START_Y,
        "player_lvl": 1,
        "player_health": 0,
        "player_bootles": 0,
        "player_money": 0,
        "player_cigarettes": 0,
        "player_score": 0,

    }
    return player


def create_boss():
    boss = {
        "boss_health": 100,
    }
    return boss


boss = create_boss()
player = create_player()


def map_creator(blank_board, MAP_NAME, LOGO_NAME, WIN, IS_RUNNING):
    global COPIED_MAP_LOCATION
    if player["player_lvl"] == 1:
        MAP_NAME = "art/mapV1.txt"
        LOGO_NAME = "art/logoV1.txt"
        COPIED_MAP_LOCATION = "tmp/mapV1.txt"
    elif player["player_lvl"] == 2:
        MAP_NAME = "art/mapV2.txt"
        LOGO_NAME = "art/logoV2.txt"
        COPIED_MAP_LOCATION = "tmp/mapV2.txt"
    elif player["player_lvl"] == 3:
        MAP_NAME = "art/mapV3.txt"
        LOGO_NAME = "art/logoV3.txt"
        COPIED_MAP_LOCATION = "tmp/mapV3.txt"
    elif player["player_lvl"] == 4:
        result = boss_scene.boss_fight(IS_RUNNING, WIN, boss, player,
                                       BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE)
        WIN = result[0]
        IS_RUNNING = result[1]
    board = engine.write_map(
        blank_board, BOARD_WIDTH, BOARD_HEIGHT, COPIED_MAP_LOCATION, MAP_PLACING_Y, MAP_PLACING_X)
    board = engine.write_map(
        blank_board, BOARD_WIDTH, BOARD_HEIGHT, LOGO_NAME, 3, 100)
    board = engine.write_map(
        blank_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 30, 10)
    board = engine.write_map(
        blank_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 10)
    board = engine.write_map(
        blank_board, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE, 5, 7)
    return board


def action_characters(board):
    if board[player["player_y"]][player["player_x"]] == "b":
        player["player_bootles"] += 1
        player["player_score"] += 10
        engine.change_field(COPIED_MAP_LOCATION,
                            MAP_PLACING_Y, MAP_PLACING_X, player, " ")
    elif board[player["player_y"]][player["player_x"]] == "f":
        player["player_cigarettes"] += 1
        player["player_score"] += 5
        engine.change_field(COPIED_MAP_LOCATION,
                            MAP_PLACING_Y, MAP_PLACING_X, player, " ")
    elif board[player["player_y"]][player["player_x"]] == "z":
        player["player_bootles"] += 1
        player["player_health"] += 20
        player["player_score"] += 20
        if player["player_health"] >= 100:
            player["player_health"] = 100
        engine.change_field(COPIED_MAP_LOCATION,
                            MAP_PLACING_Y, MAP_PLACING_X, player, " ")
    elif board[player["player_y"]][player["player_x"]] == "M":
        characters.drunkard(player, BOARD_WIDTH, BOARD_HEIGHT)
        engine.change_field(COPIED_MAP_LOCATION,
                            MAP_PLACING_Y, MAP_PLACING_X, player, " ")
    elif board[player["player_y"]][player["player_x"]] == "P":
        characters.police_man(player, BOARD_WIDTH, BOARD_HEIGHT, COPIED_MAP_LOCATION,
                              MAP_PLACING_Y, MAP_PLACING_X)
        temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        util.clear_screen()
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/lvl2.txt", 17, 55)
        ui.display_board(board)
        time.sleep(3)
    elif board[player["player_y"]][player["player_x"]] == "K":
        characters.woman(player, BOARD_WIDTH, BOARD_HEIGHT)
    elif board[player["player_y"]][player["player_x"]] == "S":
        engine.put_drunkard(COPIED_MAP_LOCATION,
                            MAP_PLACING_Y, MAP_PLACING_X, player)
        characters.shop_seller(player, BOARD_WIDTH, BOARD_HEIGHT)
    elif board[player["player_y"]][player["player_x"]] == "A":
        characters.chemist(player, BOARD_WIDTH, BOARD_HEIGHT)
        if PERM == 1:
            temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
            util.clear_screen()
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/lvl3.txt", 17, 50)
            ui.display_board(board)
            time.sleep(3)
    elif board[player["player_y"]][player["player_x"]] == "T":
        player["player_lvl"] += 1
        characters.tedi(player, BOARD_WIDTH, BOARD_HEIGHT)


def movement(board):
    global IS_RUNNING
    key = util.key_pressed()

    if key == 'q':
        IS_RUNNING = False
    elif key == "w":
        if player["player_y"] >= 2 and player["player_y"] <= BOARD_HEIGHT - 2:
            player["player_y"] -= 1
            if board[player["player_y"]][player["player_x"]] not in NOT_ALLOWED:
                action_characters(board)
            else:
                player["player_y"] += 1
    elif key == "s":
        if player["player_y"] > 0 and player["player_y"] <= BOARD_HEIGHT - 3:
            player["player_y"] += 1
            if board[player["player_y"]][player["player_x"]] not in NOT_ALLOWED:
                action_characters(board)
            else:
                player["player_y"] -= 1
    elif key == "a":
        if player["player_x"] >= 2 and player["player_x"] <= BOARD_WIDTH - 3:
            player["player_x"] -= 1
            if board[player["player_y"]][player["player_x"]] not in NOT_ALLOWED:
                action_characters(board)
            else:
                player["player_x"] += 1
    elif key == "d":
        if player["player_x"] > 0 and player["player_x"] <= BOARD_WIDTH - 4:
            player["player_x"] += 1
            if board[player["player_y"]][player["player_x"]] not in NOT_ALLOWED:
                action_characters(board)
            else:
                player["player_x"] -= 1


def choose_player(temp_board, player):
    global PLAYER_TYPE
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 5)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/ziomek_ulica.txt", 8, 25)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/ziomek_banan.txt", 8, 145)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/choose.txt", 6, 80)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/choosemenu.txt", 30, 5)
    ui.display_board(board)
    while True:
        key = util.key_pressed()
        if key == "1":
            player["player_money"] = 50
            player["player_health"] = 30
            PLAYER_TYPE = "art/ziomek_ulica.txt"
            break
        elif key == "2":
            player["player_money"] = 100
            player["player_health"] = 50
            PLAYER_TYPE = "art/ziomek_banan.txt"
            break


def main(IS_RUNNING):
    print("Can we start? Press any key to start !")
    m.getch()
    winsound.PlaySound("sound_5.wav", winsound.SND_FILENAME |
                       winsound.SND_LOOP | winsound.SND_ASYNC)
    intro_outro.intro(IS_RUNNING, BOARD_WIDTH,
                      BOARD_HEIGHT, player, PLAYER_TYPE)

    blank_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    stats_scores.score(player)
    stats_scores.boss_health(boss)
    engine.preparing_maps()
    util.clear_screen()
    board = map_creator(blank_board, MAP_NAME, LOGO_NAME,
                        WIN, IS_RUNNING)
    while IS_RUNNING:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        movement(board)
        stats_scores.score(player)
        board = map_creator(blank_board, MAP_NAME, LOGO_NAME,
                            WIN, IS_RUNNING)
        engine.put_player_on_board(board, player)
        util.clear_screen()
    intro_outro.outro(WIN, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE)


if __name__ == '__main__':
    main(IS_RUNNING)