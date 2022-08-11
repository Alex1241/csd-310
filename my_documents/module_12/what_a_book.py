#To the peer reviewers. This is not done yet. I am still working on it. 
# In its current state, it is not functional. This is will be gone, once I actually finish it and do some testing.

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def menu():
    print(" 1 - View Books \n 2 - View Store Locations \n 3 - View Your Account \n 4 Exit the Program")
    try:
        choice = int(input())
        if choice < 0 or choice > 4:
            print("Invalid number option was made. Shutting down.")
            quit()
        else:
            return choice

    except ValueError:
        print("Input invalid. Terminating Program")
        quit()

def showLoc(cursor):
    cursor.execute("SELECT store_id, locale FROM store")
    locations = cursor.fetchall()
    print("Displaying Store Locations:")
    for location in locations:
        print("Location(s):{}\n".format(location[1]))

def bookadd(cursor, user_id):
    query = ("SELECT book_id, book_name, author, details"
            "FROM book"
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {}".format(user_id))
    print(query)
    cursor.execute(query)
    canadd = cursor.fetchall()
    print("Displaying Available Books")
    for book in canadd:
        cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({},{})".format(user_id, book_id))
    print("Book added to database.")

def showBook(cursor):
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = cursor.fetchall()
    print("Showing Books")
    for book in books:
        print("Book Name: {}\n Author: {}\n Details: {}\n".format(book[1],book[2], book[3]))
    
def checkuser():
    try:
        user_id = int(input("Enter a customer id"))
        if user_id < 0 or user_id > 3:
            print("Invalid customer number detected. Shutting down.")
            quit()
        else:
            return user_id

    except ValueError:
        print("Invalid input detected. Shutting down.")
        quit()

def accmenu():
    try:
        print("Displaying customer menu")
        print(" 1 - Wishlist \n 2 - Add a Book \n 3 - Main Menu")
        accountchoice = int(input())
        if accountchoice < 0 or accountchoice > 3:
            print("Invalid input detected. Shutting down.")
            quit()
        else:
            return accountchoice
    
    except ValueError:
        print("Invalid input detected. Shutting down.")
        quit()

def addwishlist(cursor, _user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({},{})".format(_user_id, book_id))

def showwishlist(cursor, _user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
    "FROM wishlist " +
    "INNER JOIN user ON wishlist.user_id = user.user_id " +
    "INNER JOIN book ON wishlist.book_id = book.book_id " +
    "WHERE user.user_id = {}".format(_user_id))

    wishlist = cursor.fetchall()
    print("Showing Wishlist")
    for book in wishlist:
        print("Book Name: {}\n Author: {}\n".format(book[4],book[5]))

# 1 = showbook() 2 = showLoc() 3 = accmenu() 4 = quit() \\ Returned variables: choice, user_id, accountchoice
try:
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()
    print("WhatABook Application activated!")\
    
    selection = menu()
    while selection != 4:
        if selection == 1:
            showBook(cursor)
        if selection == 2:
            showLoc(cursor)
        if selection == 3:
            myID = checkuser()
            accopt = accmenu()

            while accopt != 3:
                if accopt == 1:
                    showwishlist(cursor, myID)
                if accopt == 2:
                    bookadd(cursor, myID)
                    book_id = int(input("Enter the target book's id to add"))
                    addwishlist(cursor, myID, book_id)
                    db.commit()
                    print("Book ID: {} was added to your wishlist!".format(book_id))

                accopt = accmenu()
        if selection < 0 or selection > 4:
            print("invalid option found. Please try again.")
        selection = menu()
    print("Program terminated")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()