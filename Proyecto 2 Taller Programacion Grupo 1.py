N, M, P = input().split()
N = int(N)
M = int(M)
P = int(P)
E = [["." for i in range(N)] for j in range(M)]
Px = P * 4
TE = []


def separador(input):
    strings = []
    for char in input:
        strings.append(char)
    return strings


while Px:
    Px -= 1
    TE.append(separador(str(input())))
PY = []
for i in range(0, len(TE), 4):
    submatrix = TE[i:i + 4]
    PY.append(submatrix)


def rotar(matrix):
    filas = len(matrix)
    cols = len(matrix[0])
    rotada = [[matrix[filas - 1 - j][i]
               for j in range(filas)] for i in range(cols)]
    return rotada


def espejo(matrix):
    filas = len(matrix)
    cols = len(matrix[0])
    trans = [[matrix[j][i] for j in range(filas)] for i in range(cols)]
    return rotar(trans)


def isfull(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == ".":
                return False
    return True


PL = []


def recortar(matrix):
    filas = len(matrix)
    cols = len(matrix[0])
    recorfil = [fila for fila in matrix if any(cell != '.' for cell in fila)]
    collvac = set()
    for col in range(cols):
        if all(fila[col] == '.' for fila in recorfil):
            collvac.add(col)
    recortada = [[cell for col, cell in enumerate(
        row) if col not in collvac] for row in recorfil]
    return recortada


for i in range(len(PY)):
    PL.append(recortar(PY[i]))


def ponerpiezas(E, piz, fila, col):
    k = len(piz)
    g = len(piz[0])
    for i in range(k):
        for j in range(g):
            if piz[i][j] != '.':
                if E[fila + i][col + j] != '.':
                    return False
                E[fila + i][col + j] = piz[i][j]
    return True


def remover(E, piz, fila, col):
    k = len(piz)
    g = len(piz[0])
    for i in range(k):
        for j in range(g):
            if piz[i][j] != '.':
                E[fila + i][col + j] = '.'


def isvalid(E, piz, fila, col):
    k = len(piz)
    g = len(piz[0])
    for i in range(k):
        for j in range(g):
            if piz[i][j] != '.':
                if E[fila + i][col + j] != '.':
                    return False
    return True


def adentrodelatablayaaprendiahacerestojajajajajaj(E, piz, fila, col):
    n = len(E)
    m = len(E[0])
    k = len(piz)
    g = len(piz[0])
    if fila + k > n or col + g > m:
        return False
    return True


def funccabra(PL, PTEE):
    for i in range(len(PL)):
        PTE = []
        PTE.append(rotar(PL[i]))
        PTE.append(rotar(rotar(PL[i])))
        PTE.append(rotar(rotar(rotar(PL[i]))))
        PTE.append(espejo(PL[i]))
        PTE.append(rotar(espejo(PL[i])))
        PTE.append(rotar(rotar(espejo(PL[i]))))
        PTE.append(rotar(rotar(rotar(espejo(PL[i])))))
        PTE.append(PL[i])
        PTEE.append(PTE)


PT = []
funccabra(PL, PT)


def bactrack(E, PT, i):
    if i >= len(PT) or i >= len(PT[0]):
        return False
    if not PT:
        return E
    for x in range(len(E)):
        for y in range(len(E[0])):
            for j in range(len(PT[0])):
                if adentrodelatablayaaprendiahacerestojajajajajaj(E, PT[i][j], x, y) and isvalid(E, PT[i][j], x, y):
                    ponerpiezas(E, PT[i][j], x, y)
                    if bactrack(E, PT, i+1):
                        return E
                    if isfull(E):
                        return E
                    remover(E, PT[i][j], x, y)
    return False


for row in bactrack(E, PT, 0):
    print(*row)
