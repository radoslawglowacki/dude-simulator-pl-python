import engine
import ui
import util
import time
import random
import main
import msvcrt as m
import stats_scores


def drunkard(player, BOARD_WIDTH, BOARD_HEIGHT):
    flag = True
    util.clear_screen()
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menel.txt", 3, 30)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menelmenu.txt", 30, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/meneltekst.txt", 10, 90)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
    ui.display_board(board)

    while flag:
        key = util.key_pressed()
        if key == "1":
            if player["player_money"] >= 10:
                player["player_money"] -= 10
                flag = False
                stats_scores.score(player)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menelprzyslowie.txt", 10, 90)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menel.txt", 3, 30)
                util.clear_screen()
                ui.display_board(board)
                time.sleep(3)
                return
            else:
                print("Nie masz blach, on cie nie puści, musisz zrobić z nim robote!")
        elif key == "2":
            random_int = random.randint(0, 1)
            if random_int == 0:
                player["player_score"] += 100
                player["player_cigarettes"] += 5
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menelloose.txt", 10, 90)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menel.txt", 3, 30)
                util.clear_screen()
                ui.display_board(board)
                time.sleep(3)
                return

            else:
                player["player_health"] -= 20
                player["player_bootles"] -= player["player_bootles"]
                if player["player_health"] <= 10:
                    player["player_health"] = 10
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menelwin.txt", 10, 90)
                board = engine.write_map(
                    temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/menel.txt", 3, 30)
                util.clear_screen()
                ui.display_board(board)
                time.sleep(3)
                return
        stats_scores.score(player)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 30, 150)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
        util.clear_screen()
        ui.display_board(board)


def tedi(player, BOARD_WIDTH, BOARD_HEIGHT):
    flag = True
    util.clear_screen()
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/tedi.txt", 3, 30)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/tedimenu.txt", 30, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/teditekst.txt", 10, 90)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
    ui.display_board(board)

    while flag:
        key = util.key_pressed()
        if key == "1":
            player["player_score"] += 1000
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/teditekst2.txt", 22, 95)
            board = engine.write_map(
                temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/tedi.txt", 10, 80)
            util.clear_screen()
            ui.display_board(board)
            m.getch()
            player["player_lvl"] = 4
            flag = False
        elif key == "q":
            flag = False

        util.clear_screen()
        ui.display_board(board)


def chemist(player, BOARD_WIDTH, BOARD_HEIGHT):
    global PERM
    flag = True
    util.clear_screen()
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/aptekarz.txt", 3, 30)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/aptekarzmenu.txt", 30, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/aptekarztekst.txt", 10, 90)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
    ui.display_board(board)

    while flag:
        key = util.key_pressed()
        if key == "1":
            if player["player_money"] >= 50:
                player["player_money"] -= 50
                player["player_score"] += 1000
                player["player_lvl"] = 3
                player["player_x"] = 40
                player["player_y"] = 25
                PERM = 1
            else:
                print(
                    "Czas leci a ty nie masz 9 żyć jak kot. Wracaj z pieniędzmi ziomek")
                time.sleep(3)
        elif key == "2":
            if player["player_money"] >= 50:
                player["player_money"] -= 50
                player["player_score"] += 200
                if player["player_health"] <= 100:
                    player["player_health"] += 50
            else:
                print("Nie ma siana, nie ma jarania !")
                time.sleep(2)
            if player["player_health"] >= 100:
                player["player_health"] = 100
        elif key == "q":
            flag = False

        stats_scores.score(player)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 30, 150)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
        util.clear_screen()
        ui.display_board(board)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/aptekarzprzyslowie.txt", 22, 95)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/aptekarzlogo.txt", 10, 80)
    util.clear_screen()
    ui.display_board(board)
    time.sleep(3)


def woman(player, BOARD_WIDTH, BOARD_HEIGHT):
    flag = True
    util.clear_screen()
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/kobieta.txt", 3, 30)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/kobietamenu.txt", 30, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/kobietatekst.txt", 10, 90)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
    ui.display_board(board)

    while flag:
        key = util.key_pressed()
        if key == "1":
            if player["player_money"] >= 50:
                player["player_money"] -= 50
                player["player_score"] += 100
                if player["player_health"] <= 100:
                    player["player_health"] += 20
            else:
                print("Wróć z pieniędzmi przystojniaku jak chcesz sie tak zabawić")
                time.sleep(2)
            if player["player_health"] >= 100:
                player["player_health"] = 100
        elif key == "2":
            if player["player_money"] >= 100:
                player["player_money"] -= 100
                player["player_score"] += 200
                if player["player_health"] <= 100:
                    player["player_health"] += 50
            else:
                print("Wróć z pieniędzmi przystojniaku jak chcesz sie tak zabawić")
                time.sleep(2)
            if player["player_health"] >= 100:
                player["player_health"] = 100
        elif key == "q":
            flag = False

        stats_scores.score(player)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 30, 150)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
        util.clear_screen()
        ui.display_board(board)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/kobietaprzyslowie.txt", 20, 75)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/kobietalogo.txt", 2, 10)
    util.clear_screen()
    ui.display_board(board)
    time.sleep(3)


def police_man(player, BOARD_WIDTH, BOARD_HEIGHT, COPIED_MAP_LOCATION,
               MAP_PLACING_Y, MAP_PLACING_X):
    flag = True
    util.clear_screen()
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/policjant.txt", 3, 55)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/policjantmenu.txt", 30, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/policjantlogo.txt", 5, 110)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/policjanttekst.txt", 10, 2)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
    ui.display_board(board)

    while flag:
        key = util.key_pressed()
        if key == "1":
            player["player_money"] += 100
            player["player_score"] -= 100
            engine.change_field(COPIED_MAP_LOCATION,
                                MAP_PLACING_Y, MAP_PLACING_X, player, " ")
            player["player_lvl"] += 1
            player["player_x"] = 40
            player["player_y"] = 30
            flag = False
        elif key == "2":
            player["player_money"] -= 50
            player["player_score"] += 100
            engine.change_field(COPIED_MAP_LOCATION,
                                MAP_PLACING_Y, MAP_PLACING_X, player, " ")
            player["player_lvl"] += 1
            player["player_x"] = 40
            player["player_y"] = 30
            flag = False
        elif key == "q":
            flag = False
        else:
            continue

        stats_scores.score(player)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 30, 150)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
        util.clear_screen()
        ui.display_board(board)
    time.sleep(1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/policjantprzyslowie.txt", 20, 75)
    util.clear_screen()
    ui.display_board(board)
    time.sleep(4)


def shop_seller(player, BOARD_WIDTH, BOARD_HEIGHT):
    flag = True
    util.clear_screen()
    temp_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/sprzedawca.txt", 3, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/sprzedawcamenu.txt", 30, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/sprzedawcalogo.txt", 5, 100)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/sprzedawcatekst.txt", 5, 50)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
    ui.display_board(board)

    while flag:
        key = util.key_pressed()
        if key == "q":
            flag = False
        elif key == "1":
            player["player_money"] += player["player_cigarettes"] * 5
            player["player_score"] += player["player_cigarettes"] * 5
            player["player_cigarettes"] -= player["player_cigarettes"]
        elif key == "2":
            while True:
                quantity = int(input("Podaj liczbę butelek"))
                if quantity <= player["player_bootles"]:
                    break
                else:
                    print("Podaj prawidłową ilość butelek")
                    continue
            player["player_money"] += quantity * 10
            player["player_score"] += quantity * 10
            player["player_bootles"] -= quantity
        elif key == "3":
            if player["player_money"] >= 20:
                player["player_money"] -= 20
                player["player_bootles"] += 1
                player["player_score"] += 20
                if player["player_health"] <= 100:
                    player["player_health"] += 20
                if player["player_health"] >= 100:
                    player["player_health"] = 100

        stats_scores.score(player)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score_clear.txt", 30, 150)
        board = engine.write_map(
            temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/act_score.txt", 30, 150)
        util.clear_screen()
        ui.display_board(board)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/MapClear.txt", 1, 1)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/sprzedawca.txt", 3, 10)
    board = engine.write_map(
        temp_board, BOARD_WIDTH, BOARD_HEIGHT, "art/sprzedawcaprzyslowie.txt", 5, 50)
    util.clear_screen()
    ui.display_board(board)
    time.sleep(3)
