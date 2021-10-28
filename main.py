import sys
sys.path.insert(1, 'D:/code/projects/language-practice-tool/database')

import os
import sqlite3
import queries
import review

from translations import get_string

is_running = True
db = r'./database/database.db'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Returns the menu to be printed."""
    print(get_string('activeDeck'), queries.get_deck_name())
    return (get_string('menu'))

def quit():
    """Quits the program."""
    global is_running
    is_running = False
    return get_string('goodbye')

def select_action(action):
    """Chooses the action according to the input from the user."""
    global is_running

    match action.lower():
        case '1':
            card_list = queries.view_cards()
            return review.start_review(queries)

        case '2':
            return queries.add_cards()

        case '3':
            cards = queries.view_cards()
            string = ''
            for card in cards:
                string += f'{get_string("card")} {card[0]}, {card[1]} | {card[2]}\n'
            return string

        case '4':
            return queries.choose_deck()

        case '5':
            name = input(get_string('deckName'),': ')
            return queries.new_deck(name)

        case '6':
            return queries.options()

        case '7':
            return queries.statistics()

        case '8':
            return quit()

        case _:
            return None

def main():
    try:
        connection = sqlite3.connect(db)
        queries.set_cursor(connection.cursor())

        while is_running:
            clear_screen()
            print(menu())
            action = input(get_string('selectAction'),': ')
            clear_screen()
            print(select_action(action))
    finally:
        connection.commit()
        connection.close()

if __name__ == '__main__':
    main()
