from nickname_generator import generate
from random import randint, choice


class Character:
    def __init__(self, nickname, race, age, role, sp, health, mana, stamina, skills):
        self.nickname = nickname
        self.race = race
        self.age = age
        self.role = role
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.specifications = sp
        self.skills = skills

    def show(self):
        print('Вашего персонажа зовут: ', self.nickname)
        print('Вы ', self.race, ' ваш возраст ', self.age)
        print('Умения персонажа')
        for k, v in self.specifications.items():
            print(k, v)
        print('Характеристика вашего персонажа')
        print('Здоровье ', self.health)
        print('Выносливость ', self.stamina)
        print('Мана ', self.mana)
        print('Ваше особое умение это')
        print(self.skills)


if __name__ == '__main__':
    n = int(input('Сколько людей играет: '))
    all_characters = []
    param = []
    for i in range(n):
        param.append(generate())
        param.append(choice(['Человек', 'Эльф', 'Орк', 'Гном']))
        param.append(randint(10, 100))
        param.append(choice(['Варвар', 'Бард', 'Жрец', 'Друид', 'Воин',
                             'Монах', 'Паладин', 'Рейнджер', 'Маг']))
        param.append({'Сила': randint(1, 8), 'Восприятие': randint(1, 5),
                      'Выносливость': randint(1, 8), 'Харизма': randint(1, 6),
                      'Интеллект': randint(1, 8), 'Ловкость': randint(1, 8),
                      'Удача': randint(1, 6)})
        param.append(round(randint(70, 150) + param[4]['Сила'] * 5, -1))
        param.append(round(randint(50, 110) + param[4]['Интеллект'] * 5, -1))
        param.append(round(randint(70, 130) + param[4]['Выносливость'] * 5, -1))
        param.append(choice(['Абсолютная память - мгновенное запоминание любого объема информации и долговременное '
                             'хранение её в памяти',
                             'Агностицизм - с помощью голосовых колебаний есть возможность управлять людьми и другими '
                             'существами, подчиняя себе их разум. Мало у кого есть иммунитет к этой способности, '
                             'так что, хоть особого значения она и не дает, но вот, сколько всего с ее помощью можно '
                             'сделать...',
                             'Биоэлектрическое поле – поле, которое разрушает или временно выводит из строя все'
                             ' электрические приборы в радиусе действия',
                             'Быстрота – способность передвигаться с поистине нечеловеческой скоростью.',
                             'Видение в темноте – способность, которая не нуждается в особом комментарии.',
                             'Генерация шипов на теле – возникновение из кожи ядовитых шипов – стоит оцарапать ими кожу'
                             ' другого, как тот погибает.',
                             'Замедленное старение – в организме обладателя этой способности замедлены все'
                             ' процессы старения.',
                             'Копировать чужие способности – на время или же навсегда.',
                             'Ментальный контроль - позволяет манипулировать сознанием человека/мутанта.',
                             'Создание портала – создание особого «туннеля» через который можно перемещаться с огромной'
                             ' скоростью или мгновенно. Существует как отдельная способность, так и как особый магический'
                             ' прём.',
                             ]))
        all_characters.append(Character(*param))
        param.clear()
    print('Представим каждого персонажа')
    for character in all_characters:
        character.show()
        print()
