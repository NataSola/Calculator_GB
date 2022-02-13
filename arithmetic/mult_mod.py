from fractions import Fraction

num_1 = Fraction() 
num_2 = Fraction()


def init(a,b):
    global num_1
    global num_2 
    num_1 = a
    num_2 = b
    

def do_it():
    return num_1 * num_2