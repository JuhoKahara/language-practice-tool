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
        is_active INTEGER NOT NULL,
        total_reviews INTEGER NOT NULL
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE Cards (
        cardid INTEGER PRIMARY KEY,
        front TEXT NOT NULL,
        back TEXT NOT NULL,
        last_correct_answer INTEGER,
        streak INTEGER NOT NULL,
        carddeck INTEGER NOT NULL,
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

cursor.execute('INSERT INTO Decks (name, is_active, total_reviews) VALUES ("default", 1, 0)')
cursor.execute('INSERT INTO Cards (front, back, streak, carddeck) VALUES ("test", "testi", 0, 1)')

connection.commit()
connection.close()