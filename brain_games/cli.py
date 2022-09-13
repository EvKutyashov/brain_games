import prompt


def get_user_name():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? \n')
    return print(f'Hello, {name}')


