def read_matrices_file(file_path):
    matrices = []

    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        try:
            print(f"Odczytuję linię {i}: {lines[i]}")

            rows, cols = map(int, lines[i].split())
            i += 1

            A = []
            for _ in range(rows):
                row = lines[i].split()


                if len(row) != cols:
                    raise ValueError(
                        f"Wiersz nie ma odpowiedniej liczby elementów. Oczekiwano {cols}, a otrzymano {len(row)}.")

                A.append(list(map(float, row)))
                i += 1
            b = []
            if i < len(lines):
                b = lines[i].split()
                # print(f"Wektor wyników: {b}")

                if len(b) != cols:
                    raise ValueError(f"Wektor wyników ma niewłaściwą długość. Oczekiwano {cols}, a otrzymano {len(b)}.")

                b = list(map(float, b))
                i += 1
            matrices.append((A, b))

        except (ValueError, IndexError) as e:
            print(f"Błąd w pliku przy linii {i}: {e}. Sprawdź format danych.")
            break

    return matrices