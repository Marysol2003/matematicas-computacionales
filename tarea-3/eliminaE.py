# Programa: eliminaE
# Objetivo: borra un elemento de una lista.
# Nota: borra únicamente la primera aparición del elemento.

# Ejemplos:
#   eliminaE(3, [5, 3, 2, 3])   ->  [5, 2, 3]
#   eliminaE(10, [5, 3, 2, 3])  ->  [5, 3, 2, 3]
#   eliminaE(10, [])            ->  []


def eliminaE(e, lista):
    # Caso base: si la lista está vacía, no hay nada que borrar.
    if lista == []:
        return []

    # Encontramos el elemento: lo quitamos y regresamos el resto
    # tal cual, sin seguir buscando (así solo se borra la primera vez).
    if lista[0] == e:
        return lista[1:]

    # No es el elemento: conservamos el primero y seguimos
    # buscando en el resto de la lista.
    return [lista[0]] + eliminaE(e, lista[1:])


# Pruebas
print(eliminaE(3, [5, 3, 2, 3]))    # [5, 2, 3]
print(eliminaE(10, [5, 3, 2, 3]))   # [5, 3, 2, 3]
print(eliminaE(10, []))             # []
