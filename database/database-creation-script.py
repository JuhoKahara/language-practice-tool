import sqlite3

database = r'./database.db'
connection = sqlite3.connect(database)
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Decks')
cursor.execute('DROP TABLE IF EXISTS Cards')
cursor.execute('DROP TABLE IF EXISTS Settings')

cursor.execute(
    '''
    CREATE TABLE Decks (
        deckid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        is_active INTEGER NOT NULL
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE Cards (
        cardid INTEGER PRIMARY KEY,
        front TEXT NOT NULL,
        back TEXT NOT NULL,
        last_answered TEXT,
        first_answered TEXT,
        correct_reviews INTEGER NOT NULL,
        total_reviews INTEGER NOT NULL,
        carddeck INTEGER,
        FOREIGN KEY(carddeck) REFERENCES Decks(deckid)
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE Settings (
        language TEXT,
        new_daily_card_amount INTEGER
    )
    '''
)

cursor.execute('INSERT INTO Decks (name, is_active) VALUES ("default", 1)')
cursor.execute('INSERT INTO Cards (front, back, correct_reviews, total_reviews, carddeck) VALUES ("this is an", "example card", 0, 0, 1)')

connection.commit()
connection.close()