from random import randint
import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even_game():
    name = welcome_user()
    index = 0
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while index < 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer_select = prompt.string('Your answer: ')
        answer = input()
        if (question % 2 == 0 and answer == 'yes') or (question % 2 != 0 and answer == 'no'):
            print('Correct!')
            index = index + 1
        elif question % 2 != 0 and answer == 'yes':
            print(f'''"yes" is wrong answer ;(. Correct answer was "no".
Let's try again, {name}''')
            index = index + 1
        elif question % 2 == 0 and answer == 'no':
            print(f'''"no" is wrong answer ;(. Correct answer was "yes".
Let's try again, {name}''')
            index = index + 1
    print(f'Congratulations, {name}!')
