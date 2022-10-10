import difflib


def add_word():
    while True:
        new_word = input().strip()
        if new_word == '0':
            break
        yield new_word


def check_speech(txt, list_word):
    speech = txt.split(' ')
    correct_speech = []
    cmp = {}
    for w in list_word:
        cmp[w] = difflib.get_close_matches(w, speech)
    print(cmp)
    for k, v in cmp.items():
        if not v:
            continue
        if k == v[0]:
            correct_speech.append(k)
            continue
        else:
            print('Возможно вы имели ввиду ', k, ' вместо ', v[0])
            diff = difflib.ndiff(k, v[0])
            s = ''.join(diff)
            s = s.replace(' ', '')
            tmp = ''
            i = 0
            while i < len(s):
                if s[i] == '-':
                    tmp += '?' + s[i+1] + '?'
                    i += 1
                elif s[i] == '+':
                    i += 1
                else:
                    tmp += s[i]
                i += 1
            correct_speech.append(tmp)

    return ' '.join(correct_speech)


if __name__ == '__main__':
    print('Введите слова для проверки (0 чтобы закончить): ')
    word = [i for i in add_word()]
    speech = input('Напишите свою речь: ')
    print(check_speech(speech, word))