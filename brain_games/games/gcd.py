from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round():
    num1 = randint(1, 101)
    num2 = randint(1, 101)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
