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
        answer = prompt.string('Your answer: ')
        if int(question % 2 == 0 and answer == 'yes') or int(question % 2 != 0 and answer == 'no'):
            print('Correct!')
            index = index + 1
        elif question % 2 != 0 and answer == 'yes' or answer == str(answer) and question % 2 != 0:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "no".\nLet`s try again, {name}''')
        elif question % 2 == 0 and answer == 'no' or answer == str(answer) and question % 2 == 0:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "yes".\nLet`s try again, {name}''')
    print(f'Congratulations, {name}!')
