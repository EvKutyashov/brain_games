from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_round():
    START_1 = 1
    START_2 = 101
    start_progression = randint(START_1, START_2)
    STEP_1 = 3
    STEP_2 = 5
    step = randint(STEP_1, STEP_2)
    COUNT_1 = 5
    COUNT_2 = 10
    number_count = randint(COUNT_1, COUNT_2)
    end_progression = start_progression + step * number_count
    progression = list(range(start_progression, end_progression, step))
    START_RANDOM = 0
    END_RANDOM = number_count - 1
    random_number = randint(START_RANDOM, END_RANDOM)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question += str(number) + " "
    question = str(question.strip())
    return question, correct_answer
