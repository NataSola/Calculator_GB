from fractions import Fraction


x = Fraction() 
y = Fraction()


def init(a,b):
    global x
    global y 
    x = a
    y = b
    

def do_it():
    return x * y