#!/usr/bin/python3
import random as rn 
from complex_number import ComplexNumber as cn
import re as rexpr


def parsing(text):
    token_map = ('\+', '\-', '\*', '/', '(', ')', 'i')
    split_expr = rexpr.findall('[\d.]+|[%s]' % ''.join(token_map), text)
    
    complexNumber = []
    allEq = []
    isBracket = False

    for i in range(len(split_expr)):
        if split_expr[i] == '(':
            isBracket = True
            complex = []
            w = i + 1
            while split_expr[w] != ')' and split_expr[w] != 'i':
                if '-' == split_expr[w] or '+' == split_expr[w]:
                    negative_number = split_expr[w] + split_expr[w+1]
                    complex.append(negative_number)
                    w += 2
                else:
                    complex.append(split_expr[w])
                    w += 1
            
            complexNumber.append(complex)

        elif split_expr[i] == ')':
            isBracket = False
        elif isBracket is False:
            allEq.append(split_expr[i])
    
    Complex_number_1 = cn(float(complexNumber[0][0]), float(complexNumber[0][1]))
    Complex_number_2 = cn(float(complexNumber[1][0]), float(complexNumber[1][1]))

    if '+' == allEq[0]:
        print(cn.add_complex_num(Complex_number_1, Complex_number_2))
    elif '-' == allEq[0]:
        print(cn.sub_complex_num(Complex_number_1, Complex_number_2))
    elif '*' == allEq[0]:
        print(cn.mux_complex_num(Complex_number_1, Complex_number_2))

def main():
    expr = input("Input your expression: ")
    parsed = parsing(expr)


if __name__ == "__main__":
    main()