import prompt



def welcome_user():
    name = prompt.string('May I have your name? \n')
    return print(f'Hello, {name}')


