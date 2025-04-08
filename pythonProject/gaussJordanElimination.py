from decimal import Decimal, getcontext


def jordanElimination(A, b, n, iterationNumber):

    getcontext().prec = 15


    Ab = [[Decimal(A[i][j]) for j in range(n)] + [Decimal(b[i])] for i in range(n)]
    print(f"Oryginalna macierz {iterationNumber + 1}:")
    for row in Ab:
        macierz = ["{:.1f}".format(0.0 if abs(float(x)) < 1e-12 else float(x)) for x in row[:n]]
        wyraz_wolny = "{:.1f}".format(0.0 if abs(float(row[n])) < 1e-12 else float(row[n]))
        print("[" + "  ".join(macierz) + " | " + wyraz_wolny + "]")

    for i in range(n):

        max_row = max(range(i, n), key=lambda r: abs(Ab[r][i]))
        if abs(Ab[max_row][i]) < Decimal("1e-12"):
            continue

        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

        divisor = Ab[i][i]
        Ab[i] = [x / divisor for x in Ab[i]]

        for j in range(n):
            if i != j:
                factor = Ab[j][i]
                Ab[j] = [Ab[j][k] - factor * Ab[i][k] for k in range(n + 1)]

    print(f"\nRozwiązana {iterationNumber + 1} macierz rozszerzona (w postaci zredukowanej):")
    for row in Ab:
        macierz = ["{:.1f}".format(0.0 if abs(float(x)) < 1e-12 else float(x)) for x in row[:n]]
        wyraz_wolny = "{:.1f}".format(0.0 if abs(float(row[n])) < 1e-12 else float(row[n]))
        print("[" + "  ".join(macierz) + " | " + wyraz_wolny + "]")

    for i in range(n):
        if all(abs(Ab[i][j]) < Decimal("1e-12") for j in range(n)):
            if abs(Ab[i][n]) > Decimal("1e-12"):
                print("Układ sprzeczny")
                break
            print("Układ nieoznaczony")
            break
