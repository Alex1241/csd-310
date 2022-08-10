#To the peer reviewers. This is not done yet. I am still working on it. 
# In its current state, it is not functional. This is will be gone, once I actually finish it and do some testing.

import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"pysports_user",
    "password":"MYSQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"whatabook",
    "raise_on_warnings": True
}

def menu():
    print("Press 1 to view books \n Press 2 to view store locations \n Press 3 to view your account \n Press 4 to exit the program")
    try:
        choice = int(input())
#work on this later
        if choice < 0 or choice > 3:
            print("Invalid input detected. Shutting down.")
            quit()
        elif choice == 1:
            print("")
        elif choice == 2:
            print("")
        elif choice == 3:
            print("")


    except ValueError:
        print("Input invalid. Terminating Program")
        quit()

def showLoc(cursor):
    cursor.execute("SELECT store_id, locale FROM store")
    locations = cursor.fetchall()
    print("Displaying Store Locations:")
    for location in locations:
        print("Location(s):{}\n".format(location[1]))

def bookadd(cursor, user_id, book_id):
    query = ("SELECT book_id, book_name, author, details"
            "FROM book"
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {}".format(user_id))
    print(query)
    cursor.execute(query)
    canadd = cursor.fetchall()
    print("Displaying Available Books")
    for book in canadd:
        cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({},{})".format(user_id, book_id))

def showBook(cursor):
    cursor.execute("SELECT bok_id, book_name, author, details FROM book")
    books = cursor.fetchall()
    for book in book:
        print("Book Name: {}\n Author: {}\n Details: {}\n".format(book[0],book[1], book[2]))
    
def checkuser():
    try:
        user_id = int(input("Enter a customer id"))
        if user_id < 0 or user_id > 3:
            print("Invalid customer number detected. Shutting down.")
            quit()
#work on this
        elif user_id == 1:
            print("")
        elif user_id == 2:
            print("")
        elif user_id == 3:
            print("")

    except ValueError:
        print("Invalid input detected. Shutting down.")
        quit()

def accmenu():
    try:
        print("Displaying customer menu")
        print("1 - Wishlist \n 2 - Add a Book \n 3 - Main Menu")
        accountchoice = int(input())
#work on this later
        if accountchoice < 0 or accountchoice > 3:
            print("Invalid input detected. Shutting down.")
            quit()
        elif accountchoice == 1:
            print("")
        elif accountchoice == 2:
            print("")
        elif accountchoice == 3:
            print("")
    
    except ValueError:
        print("Invalid input detected. Shutting down.")
        quit()

def addwishlist(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({},{})".format(user_id, book_id))

def showwishlist(cursor, user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author" +
    "FROM wishlist" +
    "INNER JOIN user ON wishlist.user_id = user.user_id" +
    "INNER JOIN book ON wishlist.book_id = book.book_id" +
    "WHERE user.user_id = {}".format(user_id))

    wishlist = cursor.fetchall()
    print("Showing Wishlist")
    for book in wishlist:
        print("Book Name: {}\n Author: {}\n".format(book[4],book[5]))


# Imported from previous work. Please revise later. This is the primary code that will put everything together. 
# Right now it does nothing since it was meant for connecting to pysports.
# 1 = showbook() 2 = showLoc() 3 = accmenu() 4 = quit()
try:
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("--DISPLAYING PLAYER RECORDS--")
    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()