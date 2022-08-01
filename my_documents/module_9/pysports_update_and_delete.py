import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show(cursor):
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    input("\n\n  Press any key to continue...")

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
    add = ("INSERT INTO player (first_name, last_name, team_id)"
        "VALUES('Smeagol', 'Shire Fold', 1)")
    cursor.execute(add)
    db.commit()
    print("-- Displaying Players After Insert --")
    show(cursor)

    update = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update)
    print("-- Displaying Players After Update --")
    show(cursor)
    
    delete = ("DELETE FROM player WHERE first_name = 'Smeagol'" )
    cursor.execute(delete)
    delete = ("DELETE FROM player WHERE first_name = 'Gollum'" )
    cursor.execute(delete)
    print("-- Displaying Players After Deletion --")
    show(cursor)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()

