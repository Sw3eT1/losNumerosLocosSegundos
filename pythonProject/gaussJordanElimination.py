from decimal import Decimal, getcontext


def jordanElimination(A, b, n):

    getcontext().prec = 15


    Ab = [[Decimal(A[i][j]) for j in range(n)] + [Decimal(b[i])] for i in range(n)]

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

    for i in range(n):
        if all(abs(Ab[i][j]) < Decimal("1e-12") for j in range(n)):
            if abs(Ab[i][n]) > Decimal("1e-12"):
                return "Układ sprzeczny"
            return "Układ nieoznaczony"


    return [round(float(Ab[i][n]), 6) for i in range(n)]
