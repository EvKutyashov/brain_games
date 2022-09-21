from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START_NUM_1 = 1
END_NUM_1 = 101
START_NUM_2 = 1
END_NUM_2 = 101


def get_round():
    num_1 = randint(START_NUM_1, END_NUM_1)
    num_2 = randint(START_NUM_2, END_NUM_2)
    question = f'{num_1} {num_2}'
    correct_answer = str(gcd(num_1, num_2))
    return question, correct_answer
