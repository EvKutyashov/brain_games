from prompt import string

ROUNDS_COUNT = 3


def engine(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print({game.DESCRIPTION})
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_round()
        print(f'Question: {question}')
        answer = string('Your answer:  ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
