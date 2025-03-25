def jordanElimination(A, b, n):

    Ab = [A[i] + [b[i]] for i in range(n)]

    for i in range(n):

        max_row = max(range(i, n), key=lambda r: abs(Ab[r][i]))
        if Ab[max_row][i] == 0:
            continue

        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

        divisor = Ab[i][i]
        Ab[i] = [x / divisor for x in Ab[i]]

        for j in range(n):
            if i != j:
                factor = Ab[j][i]
                Ab[j] = [Ab[j][k] - factor * Ab[i][k] for k in range(n + 1)]

    for i in range(n):
        if all(Ab[i][j] == 0 for j in range(n)):
            if Ab[i][n] != 0:
                return "Układ sprzeczny"
            return "Układ nieoznaczony"


    return [Ab[i][n] for i in range(n)]