import datetime
import random


class TimerContext(object):
    def __enter__(self):
        self.start = datetime.datetime.now()
        print(f'Контескт открыт: {self.start}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = datetime.datetime.now()
        inside = end - self.start
        print(f'Контекст закрыт: {end}')
        print(f'Внутри контекста: {inside}')


with TimerContext():
    print('Загадайте число от 0 до 100')
    start_number = 0
    final_number = 100
    have_guessed = False
    while not have_guessed:
        random_number = random.randint(start_number, final_number)
        print(f'Вы загадали число: {random_number}')
        answer = input('Загаданное число <, > или =? Введите символ:')

        if answer == '=':
            print('Я экстрасенс')
            have_guessed = True
        elif answer == '<':
            final_number = random_number - 1
        elif answer == '>':
            start_number = random_number + 1
        else:
            print('Неверный символ')




