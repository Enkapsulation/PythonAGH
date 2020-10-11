#!/usr/bin/python3
import random as rn 
import unittest

def partition(vector, first_place, last_place):
    j = (first_place - 1)
    pivot = vector[last_place]

    for i in range(first_place, last_place):
        if vector[i] <= pivot:
            j += 1
            vector[j], vector[i] = vector[i], vector[j]

    vector[j+1], vector[last_place] = vector[last_place], vector[j+1]
    return(j+1)

def quickSort(vector, first_place, last_place):
    if 1 == len(vector):
        return vector

    if first_place < last_place:
        pi = partition(vector, first_place, last_place)
 
        quickSort(vector, first_place, pi-1)
        quickSort(vector, pi+1, last_place)

class SortTest(unittest.TestCase):
    
    def test_add(self):
        v1 = [rn.randint(1, 100) for i in range(50)]
        v2 = v1
        n = len(v1)
        quickSort(v1, 0, n-1)
        v2.sort()
        print(v1)
        print(v2)
        self.assertEqual(v1, v2)


if __name__ == "__main__":
    unittest.main()