import sys
sys.path.insert(1, './')

import main
import database
import sqlite3
import pytest

# SETUP
@pytest.fixture(autouse=True)
def setup_database():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    database.set_cursor(cursor)

    cursor.execute('DROP TABLE IF EXISTS Decks')
    cursor.execute('DROP TABLE IF EXISTS Cards')

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
    yield connection

@pytest.fixture(autouse=True)
def insert_card(setup_database):
    cursor = setup_database
    cursor.execute('INSERT INTO Cards (front, back, correct_reviews, total_reviews, carddeck) VALUES ("test", "testi", 0, 0, 1)')

@pytest.fixture(autouse=True)
def setup_test_data(setup_database, insert_card):
    cursor = setup_database
    cursor.execute('INSERT INTO Decks (name, is_active) VALUES ("default", 1)')
    yield cursor

# TESTS
def test_connection(setup_test_data):
    cursor = setup_test_data
    assert len(list(cursor.execute('SELECT * FROM Decks'))) == 1
    assert len(list(cursor.execute('SELECT * FROM Cards'))) == 1

def test_menu():
    assert main.menu() == '''
        Currently active deck: default
        1. Begin review     5. New deck
        2. Add cards        6. Options
        3. View cards       7. Statistics
        4. Choose deck      8. Quit
        '''

def test_quit():
    assert main.quit() == 'Goodbye.'

def test_select_action_out_of_bounds():
    assert main.select_action('0') == None
    assert main.select_action('9') == None

# TODO
def test_select_action_one():
    assert main.select_action('1') == 'Initiating review protocol.'

def test_select_action_two(monkeypatch):
    front = 'test two'
    back = 'testi kaksi'
    responses = iter([front, back])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert main.select_action('2') == f'Added card: {front} | {back}'

def test_select_action_three():
    assert main.select_action('3') == f'Card 1, test | testi\n'

# TODO
def test_select_action_four():
    assert main.select_action('4') == 'Selecting deck.'

def test_select_action_five(monkeypatch):
    name = 'a deck of cards'
    monkeypatch.setattr('builtins.input', lambda _: name)
    assert main.select_action('5') == f'Created a new deck named {name}.'

def test_select_action_six():
    assert main.select_action('6') == 'Accessing user preferences.'

def test_select_action_seven():
    assert main.select_action('7') == 'Accessing user statistics.'

def test_select_action_eight():
    assert main.select_action('8') == 'Goodbye.'
