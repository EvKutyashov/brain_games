from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
START_NUM_1 = 1
END_NUM_1 = 101
START_NUM_2 = 1
END_NUM_2 = 101


def get_round():
    num_1 = randint(START_NUM_1, END_NUM_1)
    num_2 = randint(START_NUM_2, END_NUM_2)

    correct_answers = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
    }

    random_key = choice(list(correct_answers.keys()))
    correct_answer = str(correct_answers[random_key])
    question = f'{num_1} {random_key} {num_2}'

    return question, correct_answer
