# Programa: eliminatodo
# Objetivo: borrar todas las apariciones de un elemento en una lista.
# eliminatodo(e, lista) -> lista
#
# Ejemplos:
#   eliminatodo(3, [5, 3, 2, 3, 4, 3])  ->  [5, 2, 4]
#   eliminatodo(2, [2, 2, 2, 2])        ->  []
#   eliminatodo(4, [7, 5, 3, 7, 6])     ->  [7, 5, 3, 7, 6]
#   eliminatodo(5, [])                  ->  []


def eliminatodo(e, lista):
    # Caso base: si la lista está vacía, no hay nada que borrar.
    if lista == []:
        return []

    # El primero es el elemento: lo descartamos y seguimos
    # buscando en el resto (puede haber más apariciones).
    if lista[0] == e:
        return eliminatodo(e, lista[1:])

    # No es el elemento: lo conservamos y seguimos con el resto.
    return [lista[0]] + eliminatodo(e, lista[1:])


# Pruebas
print(eliminatodo(3, [5, 3, 2, 3, 4, 3]))   # [5, 2, 4]
print(eliminatodo(2, [2, 2, 2, 2]))         # []
print(eliminatodo(4, [7, 5, 3, 7, 6]))      # [7, 5, 3, 7, 6]
print(eliminatodo(5, []))                   # []
