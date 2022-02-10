from logging import basicConfig

# инициализация - время
# вид операции
# результат
# окончание

from datetime import datetime as dt

def calculator_fractions(data):
    time = dt.now().date
    with open('logger.csv', 'a') as file:
        file.write('')

# def calc()

# from fractions import Fraction

# choice = '+'
# num_1 = Fraction(1, 7) 
# num_2 = Fraction(5, 2) 

# def calculator_fractions(choice, num_1,num_2):

#     if choice == '+': 
#         print('{} + {} = '.format(num_1, num_2))   
#         print(num_1 + num_2) 
#     elif choice == '-': 
#         print('{} - {} = '.format(num_1, num_2)) 
#         print(num_1 - num_2) 
#     elif choice == '*': 
#         print('{} * {} = '.format(num_1, num_2)) 
#         print(num_1 * num_2) 
#     elif choice == '/': 
#         print('{} / {} = '.format(num_1, num_2)) 
#         print(num_1 / num_2) 
#     else: print('Enter a valid operator, please run the program again.')

# calculator_fractions(choice, num_1, num_2)
