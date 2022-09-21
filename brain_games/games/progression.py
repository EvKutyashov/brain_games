from random import randint

DESCRIPTION = 'What number is missing in the progression?'
START_1 = 1
START_2 = 101
STEP_1 = 3
STEP_2 = 5
COUNT_1 = 5
COUNT_2 = 10
START_RANDOM = 0
def get_round():
    start_progression = randint(START_1, START_2)
    step = randint(STEP_1, STEP_2)
    number_count = randint(COUNT_1, COUNT_2)
    end_progression = start_progression + step * number_count
    progression = list(range(start_progression, end_progression, step))
    random_number = randint(START_RANDOM, number_count - 1)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question += str(number) + " "
    question = str(question.strip())
    return question, correct_answer
