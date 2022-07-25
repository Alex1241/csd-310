#I have no idea what line 2 is, what it does, and how it got there, but the program works. I am leaving it in just in case.
from tkinter.tix import Select
import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"pysports_user",
    "password":"MYSQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n  Press any key to continue...")
    cursor = db.cursor()

    #team query
    cursor.execute("Select team_id, team_name, mascot from team")
    teams = cursor.fetchall()

    print("--DISPLAYING TEAM RECORDS--")
    for team in teams:
        print("Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team[0],team[1],team[2]))
    
    #player query
    cursor.execute(("Select player_id, first_name, last_name, team_id from player"))
    players = cursor.fetchall()

    print("--DISPLAYING PLAYER RECORDS--")
    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()





