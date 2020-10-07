#!/usr/bin/python3
import math
import random as rn 

class ComplexNumber:
    def __init__(self, real, img):
        self.re = real
        self.im = img

    def print_complex_num(self):
        if self.im < 0:
            print(f"{self.re}{self.im}i")
        else:
            print(f"{self.re} + {self.im}i")

    def module(self):
        """
        Method to module counting
        """
        return math.sqrt((self.re * self.re) - (self.im * self.im))

    def add_complex_num(com_1, com_2):
        """
        Add 2 complex number 

        com_1, com_2 -> complex number
        """
        return ComplexNumber(com_1.re + com_2.re, com_1.im + com_2.im)
        
    def sub_complex_num(com_1, com_2):
        """
        Substruct 2 complex number
        
        com_1, com_2 -> complex number
        """
        return ComplexNumber(com_1.re - com_2.re, com_1.im - com_2.im)
    
    def mux_complex_num(com_1, com_2):
        """
        multiplication 2 complex number

        com_1, com_2 -> complex number
        """
        return ComplexNumber((com_1.re * com_2.re) - (com_1.img * com_2.img), (com_1.re * com_2.img) + (com_1.img * com_2.re))

def main():
    Complex_number_1 = ComplexNumber(rn.randint(1, 10), rn.randint(1, 100))
    Complex_number_2 = ComplexNumber(rn.randint(1, 100), rn.randint(1, 100))

    Complex_number_1.print_complex_num()
    Complex_number_2.print_complex_num()
    ComplexNumber.add_complex_num(Complex_number_1, Complex_number_2).print_complex_num()

if __name__ == "__main__":
    main()