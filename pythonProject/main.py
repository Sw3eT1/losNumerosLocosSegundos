from gaussJordanElimination import jordanElimination
from readMatrixFromFile import read_matrices_file

filename = "macierze.txt"
matrices= read_matrices_file(filename)
for A, b in matrices:
    n = len(A)
    wynik = jordanElimination(A, b, n)
    print(wynik)