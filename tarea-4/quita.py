# Programa: quita
# Objetivo: quita los primeros n elementos de una lista.
# Nota: si n es mayor que el tamaño de la lista, regresa la lista vacía.

# Ejemplos:
#   quita(3, [6, 7, 2, 7, 5, 4, 2])   ->  [7, 5, 4, 2]
#   quita(10, [6, 7, 2, 7, 5, 4, 2])  ->  []
#   quita(0, [6, 7, 2])               ->  [6, 7, 2]


def quita(n, lista):
    # Caso base 1: ya no hay que quitar nada, regresamos lo que queda.
    if n <= 0:
        return lista

    # Caso base 2: la lista se vació antes de terminar de quitar
    # (pasa cuando n es más grande que la lista).
    if lista == []:
        return []

    # Quitamos el primer elemento y seguimos con el resto,
    # ahora con un elemento menos por quitar.
    return quita(n - 1, lista[1:])


# Pruebas
print(quita(3, [6, 7, 2, 7, 5, 4, 2]))    # [7, 5, 4, 2]
print(quita(10, [6, 7, 2, 7, 5, 4, 2]))   # []
print(quita(0, [6, 7, 2]))                # [6, 7, 2]
print(quita(3, [6, 7, 2]))                # []
