from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START_NUM = 1
END_NUM = 101


def get_round():
    num_1 = randint(START_NUM, END_NUM)
    num_2 = randint(START_NUM, END_NUM)
    question = f'{num_1} {num_2}'
    correct_answer = str(gcd(num_1, num_2))
    return question, correct_answer
