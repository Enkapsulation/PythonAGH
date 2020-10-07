#!/usr/bin/python3
import random as rn 


def mux_matrix(matrix_a, matrix_b):
    try:
       return [sum([matrix_a[i][j] * matrix_b[j][i] for j in range(len(matrix_a[0]))]) for i in range(len(matrix_a))]
    except:
        print("Error")

def print_matrix(matrix_a):
    print("/--------------Macierz START---------------/")
    for i in matrix_a:
        print(i)
    print("/--------------Macierz END---------------/")



m1 = [[rn.randint(1, 100) for i in range(8)] for i in range(8)]
m2 = [[rn.randint(1, 100) for i in range(8)] for i in range(8)]

print_matrix(m1)
print_matrix(m2)

result = mux_matrix(m1, m2)
print(result[0])
