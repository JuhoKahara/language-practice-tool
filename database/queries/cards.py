from translations import get_string
from . import query
import database.queries.decks as decks

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
                        OR back=:back
                        OR front=:back 
                        OR back=:front''', front.lower(), back.lower())

def add_cards():
    """Adds cards to the currently active deck"""
    is_running = 'y'

    while is_running.startswith('y'):
        front = input(get_string('front') + ': ')
        back = input(get_string('back') + ': ')

        duplicate = check_for_duplicate(front, back)

        if (front or back).startswith('!'):
            print(get_string('errorExclamationMark'))
        elif duplicate:
            id = duplicate['cardid']
            front = duplicate['front']
            back = duplicate['back']
            print(f'{get_string("errorCardTooSimilar")}. ({get_string("card")} {id}, {front} | {back})')
        else:
            query('''INSERT INTO Cards (front, back, streak, carddeck) 
                    VALUES (:front, :back, 0, 1)
                    ''', front, back
            )
            print(f'Added card: {front} | {back}')
        is_running = input(get_string('continueAdding') + '? (y/n)')
    return get_string('finishAdding')

def view_cards():
    """Displays cards in the currently active deck"""
    return query('SELECT * FROM Cards WHERE carddeck = 1')

def set_last_correct_answer(cardid: str) -> str:
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
