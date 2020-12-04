#!/usr/bin/python3
import math
import random as rn 
import unittest

class ComplexNumber:
    def __init__(self, real, img):
        self.re = real
        self.im = img

    def __setitem__(self, real, img):
        self.re = real
        self.im = img

    def __getitem__(self, real, img):
        return [self.re, self.im]

    def __str__(self):
        strCom = ""
        if self.im < 0:
            strCom = f"{self.re}{self.im}i"
        else:
            strCom = f"{self.re} + {self.im}i"
        
        return strCom

    def module(self):
        """
        Method to module counting
        """
        return float(format(math.sqrt((self.re ** 2) + (self.im ** 2)), '.1f'))

    
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
        return ComplexNumber((com_1.re * com_2.re) - (com_1.im * com_2.im), (com_1.re * com_2.im) + (com_1.im * com_2.re))

class ComplexTest(unittest.TestCase):

    def testComplexAdd(self):
        Complex_number_1 = ComplexNumber(34, 45)
        Complex_number_2 = ComplexNumber(45, 34)
        Complex_sum = ComplexNumber.add_complex_num(Complex_number_1, Complex_number_2)
        Complex_check = ComplexNumber(79, 79)

        self.assertEqual([Complex_sum.re, Complex_sum.im], [Complex_check.re, Complex_check.im])

    def testComplexSub(self):
        Complex_number_1 = ComplexNumber(56, 74)
        Complex_number_2 = ComplexNumber(13, 65)
        Complex_sub = ComplexNumber.sub_complex_num(Complex_number_1, Complex_number_2)
        Complex_check = ComplexNumber(43, 9)

        self.assertEqual([Complex_sub.re, Complex_sub.im], [Complex_check.re, Complex_check.im])

    def testComplexMux(self):
        Complex_number_1 = ComplexNumber(24, 97)
        Complex_number_2 = ComplexNumber(32, 57)
        Complex_mux = ComplexNumber.mux_complex_num(Complex_number_1, Complex_number_2)
        Complex_check = ComplexNumber(-4761, 4472)

        self.assertEqual([Complex_mux.re, Complex_mux.im], [Complex_check.re, Complex_check.im])

    def testComplexModule(self):
        Complex_number_1 = ComplexNumber(65, 87)
        Complex_number_2 = ComplexNumber(48, 36)
        
        Complex_module_1 = ComplexNumber.module(Complex_number_1)
        Complex_module_2 = ComplexNumber.module(Complex_number_2)

        self.assertEqual(Complex_module_1, 108.6)
        self.assertEqual(Complex_module_2, 60)


if __name__ == "__main__":
    unittest.main()
