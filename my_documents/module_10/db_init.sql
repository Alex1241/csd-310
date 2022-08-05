DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;

ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;

CREATE TABLE user (
	user_id	INT NOT NULL AUTO_INCREMENT,
    first_name	VARCHAR(75)	NOT NULL,
    last_name	VARCHAR(75)	NOT NULL,
    PRIMARY KEY(user_id)
    );
CREATE TABLE wishlist (
wishlist_id INT NOT NULL AUTO_INCREMENT,
user_id INT NOT NULL AUTO_INCREMENT,
book_id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(wishlist_id),
CONSTRAINT fk_user
FOREIGN KEY(user_id)
	REFERENCES user(user_id),
CONSTRAINT fk_book
FOREIGN KEY(book_id)
	REFERENCES book(book_id)
);
CREATE TABLE book (
book_id	INT NOT NULL AUTO_INCREMENT,
book_name VARCHAR(200)	NOT NULL,
details VARCHAR(500),
author VARCHAR(200)	NOT NULL,
PRIMARY KEY(book_id)
);
CREATE TABLE store (
store_id	INT NOT NULL,
locale	VARCHAR(500) NOT NULL,
PRIMARY KEY(store_id)
);



INSERT INTO store(locale)
	VALUES( );
    
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
INSERT INTO book(book_name, details, author)
	VALUES( );
    
INSERT INTO user(first_name, last_name)
	VALUES( );
INSERT INTO user(first_name, last_name)
	VALUES( );
INSERT INTO user(first_name, last_name)
	VALUES( );
    
INSERT INTO wishlist(user_id, book_id)
	VALUES( 
    (SELECT user_id FROM user WHERE first_name = ''),
    (SELECT book_id FROM book WHERE book_name = '')
    );
    
INSERT INTO wishlist(user_id, book_id)
	VALUES( 
	(SELECT user_id FROM user WHERE first_name = ''),
    (SELECT book_id FROM book WHERE book_name = '')
    
    );
INSERT INTO wishlist(user_id, book_id)
	VALUES( 
	(SELECT user_id FROM user WHERE first_name = ''),
    (SELECT book_id FROM book WHERE book_name = '')
    
    );
    