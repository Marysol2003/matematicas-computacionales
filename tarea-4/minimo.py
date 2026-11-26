def minimo(lista):
    if lista == []:
        return None
    if lista[1:] == []:
        return lista[0]
    minimo_resto = minimo(lista[1:])
    if lista[0] < minimo_resto:
        return lista[0]
    return minimo_resto


print(minimo([6, 7, 2, 7, 5, 4, 2]))
print(minimo([5]))
print(minimo([3, -8, 0, 4]))
print(minimo([1.5, 0.25, 3]))
print(minimo([]))
