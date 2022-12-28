from translations import get_string
from . import query
import database.queries.decks as decks

# Miscellaneous queries
def check_for_duplicate(front, back):
    """Checks if a word is already used in a card
        
        Args:
            front (str): The 'front' (question) of the card
            back (str): The 'back' (answer) of the card
            
        Returns:
            Query result of duplicates if there are any"""
    return query('''SELECT * 
                    FROM Cards 
                    WHERE front = :front 
                        OR back = :back
                        OR front = :back 
                        OR back = :front''', front.lower(), back.lower())

def search_card_by_text(text: str):
    """Search cards by text"""
    return query('SELECT * FROM Cards WHERE front LIKE \'%:text%\'', text)

def search_card_by_id(id: int):
    """Search cards by ID"""
    return query('SELECT * FROM Cards WHERE cardid = :id', id)

# CRUD operations
def add_card(front, back):
    """Adds a card to a deck"""
    query('''INSERT INTO Cards (front, back, streak, carddeck) 
                    VALUES (:front, :back, 0, 1)
                    ''', front, back)

def view_cards():
    """Displays cards in the currently active deck"""
    return query('SELECT * FROM Cards WHERE carddeck = 1')

def edit_cards(cardid, front, back):
    query('UPDATE Cards SET front = :front, back = :back WHERE cardid = :cardid', front, back, cardid)

def delete_cards(cardid):
    query('DELETE FROM Cards WHERE cardid = :cardid', cardid)

# Card property queries
def set_last_correct_answer(cardid: str):
    """Determines when the card was last reviewed based on the total card reviews done in the deck
        Args:
            cardid (str): the ID of the card"""
    total_reviews = decks.get_total_reviews()
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
