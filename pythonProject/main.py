from gaussJordanElimination import jordanElimination
from readMatrixFromFile import read_matrices_file

filename = "macierze.txt"
matrices = read_matrices_file(filename)

while True:
    numberOfMatrices = input("Wybierz ilość macierzy do rozwiązania: ")
    if numberOfMatrices.isnumeric() and int(numberOfMatrices) <= len(matrices):
        numberOfMatrices = int(numberOfMatrices)
        break
    else:
        print("Wprowadz poprawna wartosc numeryczna lub w zakresie ilosci macierzy")

for i in range(numberOfMatrices):
    A, b = matrices[i]
    n = len(A)
    wynik = jordanElimination(A, b, n, i)
    print("\n")
