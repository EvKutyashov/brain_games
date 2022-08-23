import random
import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_result(answer, correct_answer, name):
    if answer == str(correct_answer):
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


def get_correct_answer():
    action_lst = ['+', '-', '*']
    random_index = random.randint(0, len(action_lst) - 1)
    correct_answer = 0
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    if action_lst[random_index] == '+':
        print(f'Question: {num_1} + {num_2}')
        correct_answer = num_1 + num_2
    elif action_lst[random_index] == '-':
        print(f'Question: {num_1} - {num_2}')
        correct_answer = num_1 - num_2
    elif action_lst[random_index] == '*':
        print(f'Question: {num_1} * {num_2}')
        correct_answer = num_1 * num_2
    return correct_answer


def even_game():
    name = welcome_user()
    index = 0
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while index < 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        get_result(answer, correct_answer, name)
        index += 1
        if answer != correct_answer:
            break
        if index == 3:
            print(f'Congratulations, {name}!')


def calc_game():
    name = welcome_user()
    index = 0
    print('What is the result of the expression?')
    while index < 3:
        correct_answer = get_correct_answer()
        answer = prompt.string('Your answer: ')
        index += 1
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
        if index == 3:
            print(f'Congratulations, {name}!')
