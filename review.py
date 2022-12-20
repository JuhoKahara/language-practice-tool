from types import ModuleType
from translations import get_string

correct_answers: int = 0
database: ModuleType

def increment_correct_answers():
    global correct_answers
    correct_answers += 1

def correct_answer(card: tuple):
    database.cards.set_last_correct_answer(card[0])
    database.cards.increment_streak(card[0])
    increment_correct_answers()
    return get_string('correct') + '.\n'

def incorrect_answer(card):
    print(f'{get_string("incorrectAnswer")} {card[2]}\n')
    mark_as_correct = input(get_string('markAsCorrect') + ' (y/n)')

    if mark_as_correct.startswith('y'):
        increment_correct_answers()
        database.cards.increment_streak(card[0])
        return get_string('markedAsCorrect')
    
    database.cards.reset_last_correct_answer(card[0])
    database.cards.reset_streak(card[0])
    return get_string('markedAsIncorrect')

def display_score(card_list):
    return (get_string('score') + ':'
        f'\n{get_string("score")}: {str(correct_answers)}'
        f'/{str(len(card_list))}'
        f', {str(round(correct_answers / len(card_list), 2) * 100)} %'
        f'\n{get_string("endOfReview")}')

def start_review(db):
    global correct_answers
    global database

    database = db
    correct_answers = 0
    is_running = True
    card_list = database.cards.view_cards()

    while is_running:
        print(get_string('beginReview'))
        for card in card_list:
            print('Front: ', card[1])
            answer = input(get_string('typeAnswer') + ': ').lower()
            if answer != '!quit':
                database.decks.increment_total_reviews()
                if answer == card[2]:
                    print(correct_answer(card))
                else:
                    print(incorrect_answer(card))
            else:
                return get_string('reviewCancelled')
        is_running = False

    return display_score(card_list)


