from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d <= n / 2:
        if n % d == 0:
            return False
        d += 1
    return True


def get_round():
    START = 2
    END = 100
    random_number = randint(START, END)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
