#!/usr/bin/python3
import random as rn
import unittest 

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
                col = [sum([item[0]*item[1] for item in zip(self.data[x], matrix_transpose[y])])]
                matrix_mul[x] = col

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

class TestMatrix(unittest.TestCase):
    pass

def Test():
    matrix_1 = Matrix([[rn.randint(1, 100) for i in range(4)] for i in range(4)])
    matrix_2 = Matrix([[rn.randint(1, 100) for i in range(4)] for i in range(4)])
    
    matrix_1.print_matrix()
    matrix_2.print_matrix()
    # matrix_1.transpose()
    # matrix_1.print_matrix()
    # print(matrix_1[0, 0])
    #matrix_sum = matrix_1 + matrix_2
    #print(matrix_sum)
    
    matrix_3 = matrix_1 * matrix_2
    print(matrix_3)

if __name__ == "__main__":
    Test()