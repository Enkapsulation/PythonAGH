#!/usr/bin/python3
import random as rn
import unittest 
import numpy as np

class Matrix:
    def __init__(self, data):
        self.row = len(data)
        self.col = len(data[0])
        self.data = data

    def __setitem__(self, row, item):
        self.data[row] = item

    def __getitem__(self, row):
        return self.data[row]

    def __str__(self): 
        """ """
        row = self.row # Get the first dimension 
    
        mtxStr = ''  
        
        mtxStr += '------------- Matrix -------------\n'     
     
        for i in range(row):
         
            mtxStr += ('|' + ', '.join( map(lambda x:'{0:8.3f}'.format(x), self.data[i])) + '| \n')  
        
        mtxStr += '----------------------------------'  
        
        return mtxStr

    def __add__(self, matrix):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getMatrixSize() != matrix.getMatrixSize():
            raise "Trying to add matrixes of varying rank!"

        ret = Matrix([[0 for i in range(self.row)] for i in range(self.col)])
        
        for x in range(self.row):
            row = [sum(item) for item in zip(self.data[x], matrix[x])]
            ret[x] = row

        return ret

    def __mul__(self, matrix):
        """ Multiple a matrix with this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        matrix_row, matrix_col = matrix.getMatrixSize()
        
        if (self.row != matrix_row):
            raise "Matrices cannot be multipled!"
        
        matrix_transpose = matrix.getTranspose()
        matrix_mul = Matrix([[0 for i in range(self.row)] for i in range(self.col)])
        
        for x in range(self.col):
            for y in range(matrix_mul.row):
                matrix_mul[x][y] = sum([item[0]*item[1] for item in zip(self.data[x], matrix_transpose[y])])
                 
        return matrix_mul


    def getMatrixSize(self):
        return (self.row, self.col)

    def print_matrix(self):
        """ """
        m = self.row # Get the first dimension 
    
        mtxStr = ''  
        mtxStr += '/--------------  Matrix ---------------/\n'     
        for i in range(m):
         
            mtxStr += ('|' + ', '.join( map(lambda x:'{0:8.3f}'.format(x), self.data[i])) + '| \n')  
        mtxStr += '/--------------Matrix END---------------/\n'  
        
        print(mtxStr)

    def transpose(self):
        """ Transpose the matrix. Changes the current matrix """
        
        self.row, self.col = self.col, self.row
        self.data = [list(item) for item in zip(*self.data)]

    def getTranspose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """
        
        row, col = self.col, self.row
        mat = Matrix([[0 for i in range(4)] for i in range(4)])
        mat.data =  [list(item) for item in zip(*self.data)]

        return mat

def Test():
    m1 = Matrix([[rn.randint(1, 100) for i in range(3)] for i in range(3)])
    m2 = Matrix([[rn.randint(1, 100) for i in range(3)] for i in range(3)])
    # print(m1)
    # print(m2)        
    m3 = m1 + m2


    #Numpy to verification
    np_m1 = np.array([m1[i] for i in range(3)])
    np_m2 = np.array([m2[i] for i in range(3)])
    # print(np_m1)
    # print(np_m2)
    np_m3 = np_m1 + np_m2

    # print(np_m3)
    # self.assertTrue(Matrix([[m3[i] for i in range(3)]]) == Matrix([[np_m3[i] for i in range(3)]]))

    np_m3_conv = Matrix([[np_m3[j][i] for i in range(3)] for j in range(3)])
    print(np_m3_conv)
    print(m3)
 
if __name__ == "__main__":
    Test()
    # unittest.main()