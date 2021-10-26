import main

correct_answers = 0
database = ''

def increment_correct_answers():
    global correct_answers
    correct_answers += 1

def correct_answer(card):
    database.set_last_correct_answer(card[0])
    database.increment_streak(card[0])
    increment_correct_answers()
    return 'Correct.\n'

def incorrect_answer(card):
    print(f'Incorrect. Correct answer: {card[2]}\n')
    mark_as_correct = input('Mark as correct? (y/n)')

    if mark_as_correct.startswith('y'):
        increment_correct_answers()
        database.increment_streak(card[0])
        return 'Marked as correct.'
    
    database.reset_last_correct_answer(card[0])
    database.reset_streak(card[0])
    return 'Marked as incorrect.'

def display_score(card_list):
    return ('Score:'
        f'\nScore: {str(correct_answers)}'
        f'/{str(len(card_list))}'
        f', {str(round(correct_answers / len(card_list), 2) * 100)} %'
        '\nReview has ended.')

def start_review(db):
    global correct_answers
    global database

    database = db
    correct_answers = 0
    is_running = True
    card_list = database.view_cards()

    while is_running:
        print('Review has begun. You may quit by typing "!quit".')
        for card in card_list:
            print('Front: ', card[1])
            answer = input('Type your answer: ').lower()
            if answer != '!quit':
                database.increment_total_reviews()
                if answer == card[2]:
                    print(correct_answer(card))
                else:
                    print(incorrect_answer(card))
            else:
                return 'Review cancelled.'
        is_running = False

    return display_score(card_list)


