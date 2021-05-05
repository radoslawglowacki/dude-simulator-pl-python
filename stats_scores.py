def score(player):
    result = []
    for x in player:
        row = []
        row.append(x)
        row.append(player[x])
        result.append(row)

    with open('art/act_score.txt', 'w+') as f:
        f.write("Staty Ziomka: \n")
        f.write("\n")
        for line in result:
            line_str = ""
            if line[0] == "player_health":
                line_str += "Zdrowie:"
                line_str += " " + str(line[1])
                line_str += "\n"
            elif line[0] == "player_bootles":
                line_str += "Butelki:"
                line_str += " " + str(line[1])
                line_str += "\n"
            elif line[0] == "player_money":
                line_str += "Blachy:"
                line_str += " " + str(line[1])
                line_str += "\n"
            elif line[0] == "player_cigarettes":
                line_str += "Szlugi:"
                line_str += " " + str(line[1])
                line_str += "\n"
            elif line[0] == "player_score":
                line_str += "Wynik:"
                line_str += " " + str(line[1])
                line_str += "\n"
            f.write(line_str)


def boss_health(boss):
    result = []
    for x in boss:
        row = []
        row.append(x)
        row.append(boss[x])
        result.append(row)

    with open('art/boss_score.txt', 'w+') as f:
        f.write("Staty Stacha: \n")
        f.write("\n")
        line_str = ""
        for line in result:
            line_str = ""
            if line[0] == "boss_health":
                line_str += "Zdrowie:"
                line_str += " " + str(line[1])
                line_str += "\n"
            f.write(line_str)
