#!/usr/bin/python3
import random as rn 

# class Matrix:
#     def __init__(self, row_number, column_number):
#         self.row = row_number
#         self.col = column_number
#         self.matrix = [[rn.randint(1, 100) for i in range(self.col)] for i in range(self.row)]

#     def __matrix_sum__(matrix_a, matrix_b):
#         try:
#             return Matrix[[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
#         except:
#             print("Error, matrix must have the same length")

#     def print_matrix(self):
#         print("/--------------Matrix START---------------/")
#         for i in self.matrix:
#             print(i)
#         print("/--------------Matrix END---------------/")



class Matrix:
    def __init__(self, data):
        self.data = data

    def matrix_sum(self, matrix_b):
        try:
            print(self.data)
            print(matrix_b)
            # return Matrix([[self.data[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))])
        except:
            print("Error, matrix must have the same length")
    
    def print_matrix(self):
        print("/--------------Matrix START---------------/")
        for i in self.data:
            print(i)
        print("/--------------Matrix END---------------/")

    def __delattr__(self):
        pass

# m1 = [[rn.randint(1, 100) for i in range(128)] for i in range(128)]
# m2 = [[rn.randint(1, 100) for i in range(128)] for i in range(128)]

# print_matrix(m1)
# print_matrix(m2)
# result = matrix_sum(m1, m2)

# print(m1[87][87])
# print(m2[87][87])
# print(result[87][87])

matrix_1 = Matrix([[rn.randint(1, 100) for i in range(4)] for i in range(4)])
matrix_2 = Matrix([[rn.randint(1, 100) for i in range(4)] for i in range(4)])

matrix_1.print_matrix()
matrix_2.print_matrix()
Matrix.matrix_sum(matrix_1, 6)
