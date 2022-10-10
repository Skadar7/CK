from random import choice


def add_word():
    while True:
        new_word = input()
        if new_word == '0':
            break
        yield new_word


def gen(number_phrases, list_nouns, list_verbs):
    variants = ['nvn', 'vnn', 'nnv']
    speech = ''
    for i in range(number_phrases):
        for j in choice(variants):
            if j == 'n':
                speech += choice(nouns) + ' '
            else:
                speech += choice(verbs) + ' '
        speech = speech[:-1] + choice(['! ', '? ', '. '])
    return speech


if __name__ == '__main__':
    print('Введите существительные (0 чтобы закончить): ')
    nouns = [i for i in add_word()]
    print('Введите глаголы (0 чтобы закончить): ')
    verbs = [i for i in add_word()]
    n = int(input('Введите количетсво фраз для генерации:'))
    print(gen(n, nouns, verbs))


