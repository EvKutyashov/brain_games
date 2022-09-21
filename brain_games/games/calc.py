from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
START_NUM = 1
END_NUM = 101


def get_round():
    num_1 = randint(START_NUM, END_NUM)
    num_2 = randint(START_NUM, END_NUM)

    correct_answers = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
    }

    random_key = choice(list(correct_answers.keys()))
    correct_answer = str(correct_answers[random_key])
    question = f'{num_1} {random_key} {num_2}'

    return question, correct_answer
