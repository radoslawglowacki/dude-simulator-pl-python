import engine
import util
import ui
import main
import random
import time
import winsound


def intro_of_player(temp_board, player, PLAYER_TYPE, BOARD_WIDTH, BOARD_HEIGHT):
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 5)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loadclear.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/00.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE, 8, 60)
    if PLAYER_TYPE == "art/ziomek_ulica.txt":
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/opisulica.txt", 15, 90)
    elif PLAYER_TYPE == "art/ziomek_banan.txt":
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/opisbanan.txt", 15, 90)
    ui.display_board(board)
    time.sleep(4)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loadclear.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/11.txt", 35, 70)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loadclear.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/29.txt", 35, 70)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loadclear.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/45.txt", 35, 70)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loadclear.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/70.txt", 35, 70)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loadclear.txt", 35, 70)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/100.txt", 35, 70)
    ui.display_board(board)
    time.sleep(2)


def intro(IS_RUNNING, BOARD_WIDTH, BOARD_HEIGHT, player, PLAYER_TYPE):
    flag = True

    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/pegi.txt", 15, 85)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/gs.txt", 17, 50)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/presents.txt", 17, 70)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/mainlogo.txt", 5, 5)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/mainlogo2.txt", 10, 125)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/mainlogo3.txt", 6, 55)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/mainmenu.txt", 30, 55)
    ui.display_board(board)
    while flag:
        key = util.key_pressed()
        if key == "1":
            main.choose_player(temp_board, player)
            intro_of_player(temp_board, player, PLAYER_TYPE,
                            BOARD_WIDTH, BOARD_HEIGHT)
            flag = False
            util.clear_screen()
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/lvl1.txt", 17, 42)
            ui.display_board(board)
            time.sleep(3)
        elif key == "2":
            pass
        elif key == "q":
            flag = False
            IS_RUNNING = False


def outro(WIN, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE):
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    if WIN == 1 or WIN == 2:
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 5, 5)
        if WIN == 1:
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/boss.txt", 1, 110)
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/loose.txt", 15, 5)
        elif WIN == 2:
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE, 7, 140)
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/win.txt", 15, 5)
        ui.display_board(board)
        time.sleep(5)
        util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/end.txt", 17, 50)
    ui.display_board(board)
    time.sleep(3)
    util.clear_screen()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    exit()
