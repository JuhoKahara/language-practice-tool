import sqlite3

cursor = ''

# Card queries
def check_for_duplicate(front, back):
    return query('''SELECT * FROM Cards 
                                    WHERE front=:front OR back=:back
                                    OR front=:back OR back=:front
                                    ''', front.lower(), back.lower())

def add_cards():
    """Adds cards to the currently active deck."""
    is_running = 'y'

    while is_running.startswith('y'):
        front = input('Front: ')
        back = input('Back: ')

        duplicate = check_for_duplicate(front, back)

        if (front or back).startswith('!'):
            print('A card may not start with an exclamation mark (!)')
        elif duplicate:
            id = duplicate['cardid']
            front = duplicate['front']
            back = duplicate['back']
            print(f'Card is too similar to another card. (Card {id}, {front} | {back})')
        else:
            query('''INSERT INTO Cards (front, back, streak, carddeck) 
                    VALUES (:front, :back, 0, 1)
                    ''', front, back
            )
            print(f'Added card: {front} | {back}')
        is_running = input('Continue adding cards? (y/n)')
    return 'Finished adding cards.'

def view_cards():
    """Display cards in the currently active deck."""
    return query('SELECT * FROM Cards WHERE carddeck = 1')

def set_last_correct_answer(cardid):
    """Used to determine when the card was last reviewed based on the total card reviews done in the deck."""
    total_reviews = get_total_reviews()
    query('UPDATE Cards SET last_correct_answer = :total_reviews WHERE cardid = :cardid', total_reviews[0][0], cardid)

def reset_last_correct_answer(cardid):
    """Resets the last_correct_answer value to Null"""
    query('UPDATE Cards SET last_correct_answer = NULL WHERE cardid = :cardid', cardid)

def get_last_correct_answer(cardid):
    """Returns the review count of when the specified card was last answered correctly."""
    return query('SELECT last_correct_answer FROM Cards WHERE cardid = :cardid', cardid)[0]

def get_streak(cardid):
    return query('SELECT streak FROM Cards WHERE cardid = :cardid', cardid)[0]

def increment_streak(cardid):
    query('UPDATE Cards SET streak = streak + 1 WHERE cardid = :cardid', cardid)

def reset_streak(cardid):
    query('UPDATE Cards SET streak = 0 WHERE cardid = :cardid', cardid)

# Deck queries
def choose_deck():
    """Selects the deck to set as currently active."""
    query_result = query('SELECT * FROM Decks')
    for row in query_result:
        print(row)
    return 'Selecting deck.'

def new_deck(name):
    """Creates a new deck."""
    query('INSERT INTO Decks (name, is_active, total_reviews) VALUES (:name, 0, 0)', name)
    return f'Created a new deck named {name}.'

def get_deck_name():
    """Returns the name of the currently active deck."""
    return query('SELECT name FROM Decks WHERE is_active = 1')[0][0]

def get_total_reviews():
    return query('SELECT total_reviews FROM Decks WHERE is_active = 1')

def increment_total_reviews():
    query('UPDATE Decks SET total_reviews = total_reviews + 1 WHERE is_active = 1')

# Other stuff
def options():
    """Provides access to user preferences."""
    return 'Accessing user preferences.'

def statistics():
    """Returns statistics of past user performance."""
    return 'Accessing user statistics.'

def set_cursor(c):
    global cursor
    cursor = c

def query(query, *args):
    if args:
        return cursor.execute(query, args).fetchone()
    else:
        return cursor.execute(query).fetchall()

    
