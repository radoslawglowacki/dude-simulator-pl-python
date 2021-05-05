import ui
import util
import main
import engine
import time
import random
import msvcrt as m
import stats_scores


def boss_fight(IS_RUNNING, WIN, boss, player, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE):
    flag = True

    stats_scores.score(player)
    stats_scores.boss_health(boss)
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()

    # SCENE 1
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/poziomfinal.txt", 17, 45)
    ui.display_board(board)
    time.sleep(2)
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/bosslogo.txt", 17, 25)
    ui.display_board(board)
    time.sleep(2)

    # SCENE 2
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/boss.txt", 1, 100)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE, 10, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/bosstekst.txt", 4, 60)
    ui.display_board(board)
    m.getch()

    # SCENE 3
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/boss.txt", 1, 100)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE, 10, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/playertekst.txt", 10, 35)
    ui.display_board(board)
    m.getch()

    # SCENE 4
    util.clear_screen()
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/bossfight.txt", 15, 65)
    ui.display_board(board)
    time.sleep(2)

    # FIGHT SCENE
    while flag:
        util.clear_screen()
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/boss.txt", 1, 100)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, PLAYER_TYPE, 10, 20)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 5, 2)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 5, 5)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/boss_score_clear.txt", 5, 170)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/boss_score.txt", 5, 170)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/ciosy.txt", 34, 5)
        ui.display_board(board)

        key = util.key_pressed()
        miss_or_not = random.randint(0, 1)
        if key == "1":
            if miss_or_not == 0:
                print("Nie trafileś !")
            if miss_or_not == 1:
                boss["boss_health"] = boss["boss_health"] - 5
                print("Siadło !")
        elif key == "2":
            if miss_or_not == 1:
                print("Nie trafileś !")
            else:
                boss["boss_health"] -= 10
                print("Siadło !")
        elif key == "3":
            if player["player_bootles"] >= 1:
                if miss_or_not == 2:
                    print("Nie trafileś !")
                else:
                    boss["boss_health"] -= 20
                    player["player_bootles"] -= 1
                    print("Siadło !")
            else:
                print("Nie masz butelek, zmarnowales ruch !")
        elif key == "c":
            correct_cheat = "legiawarszawa"
            user_cheat = input("Nie za łatwo bedzie? Dawaj juz ten kod: ")
            if correct_cheat == user_cheat:
                boss["boss_health"] -= 50
            else:
                print("Nawet kodu nie umiesz wpisac a chcesz walczyc ze Stachem..")
        time.sleep(1)

        what_hit_from_boss_now = random.randint(1, 2)
        miss_or_not = random.randint(0, 1)
        if what_hit_from_boss_now == 1:
            if miss_or_not == 0:
                print("Nieźle, taki jesteś niuchwytny albo on pijany. Nie trafił !")
            elif miss_or_not == 1:
                player["player_health"] -= 5
                print("Nic ci nie bedzie, nie becz")
        elif what_hit_from_boss_now == 2:
            if miss_or_not == 0:
                print("Nieźle, taki jesteś niuchwytny albo on pijany. Nie trafił !")
            elif miss_or_not == 1:
                player["player_health"] -= 10
                print("Żyjesz? Wstawaj, nie badz lamus")
        time.sleep(2)

        if player["player_health"] <= 0:
            player["player_health"] = 0
            WIN = 1
            flag = False
        elif boss["boss_health"] <= 0:
            boss["boss_health"] = 0
            WIN = 2
            flag = False

        stats_scores.score(player)
        stats_scores.boss_health(boss)
    IS_RUNNING = False

    return WIN, IS_RUNNING
