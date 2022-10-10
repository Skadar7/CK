from datetime import datetime, timedelta
from time import sleep


def check_timer(h, m, s):
    timer = datetime.now() + timedelta(hours=h, minutes=m, seconds=s)
    while True:
        now = datetime.now() + timedelta(milliseconds=1)
        if now.strftime('%H:%M:%S') != timer.strftime('%H:%M:%S'):
            cur_t = str((timer - now) + timedelta(seconds=1))[:-7]
            print('Осталось времени: {}'.format(cur_t))
            sleep(1)
        else:
            print('Время вышло!')
            break


if __name__ == '__main__':
    print('Установим таймер\n')
    hours = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    seconds = int(input('Введите секунды: '))
    check_timer(hours, minutes, seconds)