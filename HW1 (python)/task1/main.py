priority = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '^': 3,
    '#': 3  # Извлечение корня
}

brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class Calculator:
    def __init__(self, exp):
        self.postfix = None
        self.result = None
        self.exp = exp

    def convert(self):
        infix_string = '(' + self.exp + ')'
        postfix = ''
        stack = []
        buf = ''
        try:
            for i in infix_string:
                if i.isdigit():
                    buf += i
                elif len(buf) > 0:
                    postfix += buf + ' '
                    buf = ''
                elif i.isalpha():
                    print('Ошибка, неверное значение ', i,
                          'символ ', infix_string.find(i) - 1)
                    raise ValueError

                if i in priority.keys() and i not in brackets.keys():
                    while stack and priority[i] <= priority[stack[-1]]:
                        postfix += stack.pop() + ' '
                    if postfix[-2] == i:
                        print('Ошибка, неверный оператор ', i,
                          'символ ', infix_string.find(i) - 1)
                        raise ValueError
                    stack.append(i)
                elif i in brackets.keys():
                    stack.append(i)
                elif i in brackets.values():
                    while stack and stack[-1] not in brackets.keys():
                        postfix += stack.pop() + ' '
                    if stack:
                        del stack[-1]
                elif i not in priority.keys() and not i.isdigit():
                    print('Ошибка, неверное значение ', i,
                          'символ ', infix_string.find(i) - 1)
                    raise ValueError
        except ValueError:
            return 'Error'

        self.postfix = postfix
        return self.calculate()

    def calculate(self):
        buf = ''
        stack = []
        try:
            for i in self.postfix:
                if i.isdigit():
                    buf += i
                elif len(buf) > 0:
                    stack.append(buf)
                    buf = ''
                if i in priority.keys() and i not in brackets.keys():
                    if len(stack) > 1:
                        a = float(stack.pop())
                        b = float(stack.pop())
                        stack.append(self.calc(b, a, i))
            return stack.pop()
        except ValueError:
            return 'Error'

    def calc(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        elif operator == '^':
            return a ** b
        elif operator == '%':
            return a % b
        elif operator == '#':
            return a ** (1 / b)
        else:
            return 'Error'


if __name__ == '__main__':
    print('Операторы:\n', '+ Сложить\n', '- Вычесть\n', '* Умножить\n',
          '/ Разделить\n', '% Остаток от деления\n', '^ Возведение в степень\n',
          '# Извлечь корень\n')
    exp = input('Введите выражение (без пробелов): ')
    calculator = Calculator('(' + exp + ')')
    print('Результат =', calculator.convert())
