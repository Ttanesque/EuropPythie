import sqlite3

DB = sqlite3.connect("EuroPythie.sqlite")


def init() -> None:
    cursor = DB.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS games (id integer primary key autoincrement, name text, date_creation date, players text)"
    )
    cursor.close()


def getGames() -> list:
    cursor = DB.cursor()
    res = []

    raw_games = cursor.execute("SELECT * FROM games").fetchall()
    for raw_game in raw_games:
        res.append(Game(*raw_game))
    
    cursor.close()
    return res

def saveGames(name: str, date_creation: str, players: str) -> None:
    cursor = DB.cursor()

    cursor.execute("INSERT INTO games (name, date_creation, players) VALUES (?, ?, ?)", (name, date_creation, players))
    DB.commit()

    cursor.close()


class Game:
    def __init__(self, id: int, name: str, date_creation:str, players: str) -> None:
        self.id = id
        self.name = name
        self.date_creation = date_creation
        self.players = players.split(",")

    def __str__(self) -> str:
        players = " ".join(self.players)
        return str.format("{}\t{}\t{}", self.date_creation, self.name, players)
