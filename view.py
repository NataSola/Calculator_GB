from fractions import Fraction
import sys

def get_value():
    return Fraction(input('Введите число: '))

def get_operator():
    return input('Введите оператор: ')

def get_result(res):
    print(res)