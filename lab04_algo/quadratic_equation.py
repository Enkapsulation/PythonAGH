#!/usr/bin/python3
import math

def quadratic_equation(a, b, c):
    #delta
    delta = (b**2) - (4 * a * c)

    #miejsca zerowe
    try:
        if 0 > delta:
            return "Nie ma"
        elif 0 == delta:
            x_0 = -b/(2*a)
            return [x_0, x_0]
        else:
            x_1 = ((-b - math.sqrt(delta))/(2*a)) 
            x_2 = ((-b + math.sqrt(delta))/(2*a))
            return [x_1, x_2]
    except:
        print("Error, something went wrong!")

def Test():
    a, b, c = input("Podaj współczynniki a b c w postaci ax^2 + bx + c: ").split()
    x_1 = quadratic_equation(int(a),int(b),int(c))

    if x_1[0] == x_1[1]:
        print(f'Jedno miejsce zerowe w x = {x_1[0]}')
    elif "Nie ma" == x_1:
        print("Nie ma miejsc zerowych")
    else:
        print(f'Dwa miejsca zerowe w x1 = {x_1[0]} i x2 = {x_1[1]}')

if __name__ == "__main__":
    Test()