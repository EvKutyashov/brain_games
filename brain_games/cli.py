import prompt


def get_user_name():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


