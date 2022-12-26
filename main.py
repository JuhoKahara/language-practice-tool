import os
import sys
import sqlite3
import database.queries
import database.queries.cards as cards
import database.queries.decks as decks
import database.queries.others as others
import review

from translations import get_string

sys.path.insert(1, os.getcwd() + '/database')
is_running = True
db = r'./database/database.db'

def clear_screen():
    """Clears the console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Prints the menu
        Returns: 
            The menu (str) to be printed"""
    print(get_string('currentlyActiveDeck'), decks.get_deck_name())
    return get_string('menu')

def quit():
    """Quits the program
        Returns:
            A string with a heartfelt farewell message"""
    global is_running
    is_running = False
    return get_string('goodbye')

def add_cards():
    """A loop for adding cards to the currently active deck"""
    is_running = 'y'

    while is_running.startswith('y'):
        front = input(get_string('front') + ': ')
        back = input(get_string('back') + ': ')

        duplicate = cards.check_for_duplicate(front, back)
        print(duplicate)

        if (front or back).startswith('!'):
            print(get_string('errorExclamationMark'))
        elif duplicate:
            id = duplicate[0]
            front = duplicate[1]
            back = duplicate[2]
            print(f'{get_string("errorCardTooSimilar")}. ({get_string("card")} {id}, {front} | {back})')
        else:
            cards.add_card(front, back)
            print(f'Added card: {front} | {back}')
        is_running = input(get_string('continueAdding') + '? (y/n)')
    return get_string('finishAdding')

def select_action(action: str) -> str:
    """Chooses the action according to the input from the user
        Args:
            action (str): the action chosen by the user of the program"""
    global is_running

    match action.lower():
        case '1':
            return review.start_review(database.queries)

        case '2':
            return add_cards()

        case '3':
            card_list = cards.view_cards()
            string = ''
            for card in card_list:
                string += f'{get_string("card")} {card[0]}, {card[1]} | {card[2]}\n'
            return string

        case '4':
            return decks.choose_deck()

        case '5':
            name = input(get_string('deckName') + ': ')
            return decks.new_deck(name)

        case '6':
            return others.options()

        case '7':
            return others.statistics()

        case '8':
            return quit()

        case _:
            return None

def main():
    """The main loop"""
    try:
        connection = sqlite3.connect(db)
        database.queries.set_cursor(connection.cursor())

        while is_running:
            clear_screen()
            print(menu())
            action = input(get_string('selectAction') + ': ')
            clear_screen()
            print(select_action(action))
            if action != '8':
                input(get_string('returnToMenu') + ' ')
    finally:
        connection.commit()
        connection.close()

if __name__ == '__main__':
    main()
