correct_answers = 0

def start_review(card_list):
    correct_answers = 0
    is_running = True

    while is_running:
        for card in card_list:
            print(card[1])
            answer = input('Type your answer: ').lower()
            if answer == card[2]:
                print(correct_answer())
            else:
                print(f'Incorrect. Correct answer: {card[2]}')
        is_running = False

    return((
        f'Score: {str(correct_answers)}'
        f'/{str(len(card_list))}'
        f', {str(round(correct_answers / len(card_list), 2) * 100)} %'
        )
    )

def correct_answer():
    global correct_answers
    correct_answers += 1
    return 'Correct.'
