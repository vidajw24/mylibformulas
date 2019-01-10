
import math

def fibon_sequence(n): # This is the defintion of the function
    x = 1
    y = 1

    cont = 1
    while cont <= n: # n is the parameter of the function, that should be given
                     # when the function is called
        print('A new Fibon number is: ', x + y)
        temp = x
        x = y
        y = y + temp

        cont = cont + 1

def swap(a, b):
    temp = a
    a = b
    b = temp
    return print(a, b)

