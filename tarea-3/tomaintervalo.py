# Programa: tomaintervalo
# Objetivo: toma un segmento de una lista a partir de un intervalo [a, b].
#           Los índices empiezan en 0, como en Python.
#
# Ejemplo:
#   tomaintervalo(2, 3, ['a', 'b', 'c', 'd'])  ->  ['c', 'd']


def tomaintervalo(a, b, lista):
    # Caso base: si la lista está vacía o ya pasamos el final del
    # intervalo (b < 0), no hay nada más que tomar.
    if lista == [] or b < 0:
        return []

    # Todavía no llegamos al inicio del intervalo:
    # descartamos el primer elemento y "recorremos" el intervalo
    # una posición (a - 1, b - 1) para seguir con el resto de la lista.
    if a > 0:
        return tomaintervalo(a - 1, b - 1, lista[1:])

    # Ya estamos dentro del intervalo (a == 0):
    # guardamos el primer elemento y pedimos el resto recursivamente.
    return [lista[0]] + tomaintervalo(0, b - 1, lista[1:])


# Pruebas
print(tomaintervalo(2, 3, ['a', 'b', 'c', 'd']))   # ['c', 'd']
print(tomaintervalo(0, 1, ['a', 'b', 'c', 'd']))   # ['a', 'b']
print(tomaintervalo(1, 1, ['a', 'b', 'c', 'd']))   # ['b']
print(tomaintervalo(0, 3, ['a', 'b', 'c', 'd']))   # ['a', 'b', 'c', 'd']
