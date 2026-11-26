# Programa: minimo
# Objetivo: regresa el elemento más pequeño de una lista de números.
# Nota: una lista vacía no tiene mínimo; en ese caso regresa None.

# Ejemplos:
#   minimo([6, 7, 2, 7, 5, 4, 2])  ->  2
#   minimo([5])                    ->  5
#   minimo([3, -8, 0, 4])          ->  -8
#   minimo([])                     ->  None


def minimo(lista):
    # Caso especial: la lista vacía no tiene elementos, no hay mínimo.
    if lista == []:
        return None

    # Caso base: si solo queda un elemento, ese es el mínimo.
    if lista[1:] == []:
        return lista[0]

    # Buscamos el mínimo del resto de la lista y lo comparamos
    # con el primer elemento; nos quedamos con el más pequeño.
    minimo_resto = minimo(lista[1:])
    if lista[0] < minimo_resto:
        return lista[0]
    return minimo_resto


# Pruebas
print(minimo([6, 7, 2, 7, 5, 4, 2]))   # 2
print(minimo([5]))                     # 5
print(minimo([3, -8, 0, 4]))           # -8
print(minimo([1.5, 0.25, 3]))          # 0.25
print(minimo([]))                      # None
