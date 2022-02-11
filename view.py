from fractions import Fraction

def get_value():
    return Fraction(input('Введите дробь: '))

def get_operator():
    return input('Введите оператор: ')

def get_result(res):
    print(f'Результат: {Fraction(res)}')
