import sys
sys.path.insert(1, './database')

import sqlite3
import database
import review

is_running = True
db = r'./database/database.db'

def menu():
    """Returns the menu to be printed."""
    return (
        f'''
        Currently active deck: {database.get_deck_name()}
        1. Begin review     5. New deck
        2. Add cards        6. Options
        3. View cards       7. Statistics
        4. Choose deck      8. Quit
        '''
        )

def quit():
    """Quits the program."""
    global is_running
    is_running = False
    return 'Goodbye.'

def select_action(action):
    """Chooses the action according to the input from the user."""
    global is_running

    match action.lower():
        case '1':
            card_list = database.view_cards()
            return review.start_review(database)

        case '2':
            front = input('Front: ')
            back = input('Back: ')
            return database.add_card(front, back)

        case '3':
            cards = database.view_cards()
            string = ''
            for card in cards:
                string += f'Card {card[0]}, {card[1]} | {card[2]}\n'
            return string

        case '4':
            return database.choose_deck()

        case '5':
            name = input('Deck name: ')
            return database.new_deck(name)

        case '6':
            return database.options()

        case '7':
            return database.statistics()

        case '8':
            return quit()

        case _:
            return None

def main():
    try:
        connection = sqlite3.connect(db)
        database.set_cursor(connection.cursor())

        while is_running:
            print(menu())
            action = input('Select action: ')
            print(select_action(action))
    finally:
        connection.commit()
        connection.close()

if __name__ == '__main__':
    main()
