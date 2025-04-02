from gaussJordanElimination import jordanElimination
from readMatrixFromFile import read_matrices_file

filename = "macierze.txt"
matrices= read_matrices_file(filename)

# for matrix in matrices:
#     print(matrix)

for A, b in matrices:
    n = len(A)
    wynik = jordanElimination(A, b, n)
    print(wynik)