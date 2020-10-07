#!/usr/bin/python3
import random as rn

def scalar(vector_1, vector_2):
    try:
        return sum([vector_1[i] * vector_2[i] for i in range(len(vector_1))])
    except:
        print("Error, vector must have the same length")
        
        
v1 = [rn.randint(1, 100) for i in range(4)]
v2 = [rn.randint(1, 100) for i in range(4)]

print(v1)
print(v2)

v3 = scalar(v1, v2)

if None != v3:
    print(f'Scalar: {v3}')
