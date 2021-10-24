import sqlite3

cursor = ''

def add_card(front, back):
    """Adds cards to the currently active deck.
    :param front: Determines what is displayed on the front side of the card
    :param back: Determines what is displayed on the back side of the card
    """
    check_for_duplicate = query('''SELECT * FROM Cards 
                                WHERE front=:front OR back=:back
                                OR front=:back OR back=:front
                                ''', front.lower(), back.lower())

    if check_for_duplicate:
        id = check_for_duplicate[0]
        front = check_for_duplicate[1]
        back = check_for_duplicate[2]
        return f'Card is too similar to another card. (Card {id}, {front}:{back})'
    else:
        query('''INSERT INTO Cards (front, back, correct_reviews, total_reviews, carddeck) 
                VALUES (:front, :back, 0, 0, 1)
                ''', front, back
                )
        return f'Added card: {front} | {back}'

def view_cards():
    """Display cards in the currently active deck."""
    return query('SELECT * FROM Cards WHERE carddeck = 1')

def choose_deck():
    """Selects the deck to set as currently active."""
    query_result = query('SELECT * FROM Decks')
    for row in query_result:
        print(row)
    return 'Selecting deck.'

def new_deck(name):
    """Creates a new deck."""
    query('INSERT INTO Decks (name, is_active) VALUES (:name, 0)', name)
    return f'Created a new deck named {name}.'

def options():
    """Provides access to user preferences."""
    return 'Accessing user preferences.'

def statistics():
    """Returns statistics of past user performance."""
    return 'Accessing user statistics.'

def review():
    """Starts the review process."""
    return 'Initiating review protocol.'

def get_deck_name():
    """Returns the name of the currently active deck."""
    return query('SELECT name FROM Decks WHERE is_active = 1')[0][0]

def set_cursor(c):
    global cursor
    cursor = c

def query(query, *args):
    if args:
        return cursor.execute(query, args).fetchone()
    else:
        return cursor.execute(query).fetchall()

    
