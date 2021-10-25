correct_answers = 0

def start_review(database):
    global correct_answers
    correct_answers = 0
    is_running = True
    card_list = database.view_cards()

    while is_running:
        for card in card_list:
            print(card[1])
            answer = input('Type your answer: ').lower()
            if answer == card[2]:
                print(correct_answer())
            else:
                print(f'Incorrect. Correct answer: {card[2]}\n')
        is_running = False

    return((
        'This was the last card. Below you will see your score.'
        f'\nScore: {str(correct_answers)}'
        f'/{str(len(card_list))}'
        f', {str(round(correct_answers / len(card_list), 2) * 100)} %'
        '\nReview has ended.'
        )
    )

def correct_answer():
    global correct_answers
    correct_answers += 1
    return 'Correct.\n'
