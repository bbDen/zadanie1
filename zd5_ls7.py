num = 35372


def find_sum(num):
    if isinstance(num, int):
        a = num % 10
        n = num // 10
        b = num % 10
        n = num // 10
        c = num % 10
        n = num // 10
        d = num % 10
        n = num // 10
        e = num % 10
        return f'Сумма цифр числа: {a + b + c + d + e}'
    else:
        return 'Вы ввели неверное значение'
