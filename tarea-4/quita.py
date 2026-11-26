def quita(n, lista):
    if n <= 0:
        return lista
    if lista == []:
        return []
    return quita(n - 1, lista[1:])


print(quita(3, [6, 7, 2, 7, 5, 4, 2]))
print(quita(10, [6, 7, 2, 7, 5, 4, 2]))
print(quita(0, [6, 7, 2]))
print(quita(3, [6, 7, 2]))
