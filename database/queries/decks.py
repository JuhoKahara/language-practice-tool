from translations import get_string
from . import query

# Miscellaneous queries
def choose_deck():
    """Selects the deck to set as currently active."""
    query_result = query('SELECT * FROM Decks')
    for row in query_result:
        print(row)
    return None

# CRUD operations
def new_deck(name):
    """Creates a new deck."""
    query('INSERT INTO Decks (name, is_active, total_reviews) VALUES (:name, 0, 0)', name)
    return f'{get_string("createdDeck")} {name}.'

def view_decks():
    """Displays all decks"""
    query('SELECT * FROM Decks')

def edit_deck(deckid, name):
    """Edit deck"""
    query('UPDATE Decks SET name = :name WHERE deckid = :deckid', name, deckid)

def delete_deck(deckid):
    """Deletes a deck"""
    query('DELETE FROM Decks WHERE deckid = :deckid', deckid)

# Deck propery queries
def get_deck_name():
    """Returns the name of the currently active deck."""
    return query('SELECT name FROM Decks WHERE is_active = 1')[0][0]

def get_total_reviews():
    return query('SELECT total_reviews FROM Decks WHERE is_active = 1')

def increment_total_reviews():
    query('UPDATE Decks SET total_reviews = total_reviews + 1 WHERE is_active = 1')