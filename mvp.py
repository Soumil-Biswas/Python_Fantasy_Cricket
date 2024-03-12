import sqlite3
import random

library = sqlite3.connect('Players.db')
cur = library.cursor()


def evaluate(i):
    cur.execute("SELECT * FROM stats WHERE Player = '" + i + "';")
    data = cur.fetchall()
    print(data)
    for row in data:
        name = (row[0])
        matches = (row[1])
        runs = (row[2])
        hundreds = (row[3])
        fifties = (row[4])
        value = (row[5])
        ctg = (row[6])

    cur.execute("SELECT * FROM match WHERE Player = '" + i + "';")
    data2 = cur.fetchall()
    print(data2)
    for row in data2:
        scored = (row[1])
        faced = (row[2])
        fours = (row[3])
        sixes = (row[4])
        bowled = (row[5])
        maiden = (row[6])
        given = (row[7])
        wkts = (row[8])
        catching = (row[9])
        stumping = (row[10])
        runouts = (row[11])

    Bat = int(bat(scored, faced, fifties, hundreds, fours, sixes))
    Bow = int(bowl(wkts, bowled, given))
    Field = int(field(catching, stumping, runouts))

    total_score = Bat + Bow + Field
    rand = random.uniform(0.9, 2)
    total_score = int(total_score * rand)
    print("total score of {} is {}" .format(i, total_score))

    return total_score


# Score Calculation Module (Bat)
def bat(scored, faced, fifties, hundreds, fours, sixes):
    pts = 0

    pts = pts + (scored / 2)
    strike_rate = (scored / faced) * 100

    pts = pts + (fifties * 5)
    pts = pts + (hundreds * 10)

    if strike_rate > 80:
        pts = pts + 2
        if strike_rate > 100:
            pts = pts + 4

    pts = pts + (fours * 1)
    pts = pts + (sixes * 2)

    pts = pts/10
    print("Battling points = {}" .format(pts))
    return pts


# Score Calculation Module (Bowl)
def bowl(wkts, bowled, given):
    pts = 0
    pts = pts + (wkts * 10)
    overs = int(bowled/ 6)
    try:
        economy = (given / overs)
    except:
        economy = 0

    if wkts >= 3:
        pts = pts + 5
        if wkts >= 5:
            pts = pts + 10
    if economy < 4.6:
        pts = pts + 4
    elif economy < 3.6:
        pts = pts + 7
    elif economy < 2.1:
        pts = pts + 10

    print("Bowling points = {}".format(pts))
    return pts


# Score Calculation Module (Field)
def field(catching, stumping, runouts):
    pts = 0

    fiel = catching + stumping + runouts
    pts = pts + (fiel * 10)

    print("Fielding points = {}".format(pts))
    return pts


evaluate("Dhoni")





