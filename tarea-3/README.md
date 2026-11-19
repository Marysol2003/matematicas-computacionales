# Tarea 3: programación recursiva

Alumna: Marysol Segueda
Materia: Matemáticas Computacionales

Video con la explicación: [pendiente]

## Programas

| Archivo | Qué hace | Ejemplo |
|---|---|---|
| [tomaintervalo.py](tomaintervalo.py) | Toma los elementos de una lista entre las posiciones `a` y `b`, incluyendo ambas | `tomaintervalo(2, 3, ['a','b','c','d'])` → `['c', 'd']` |
| [eliminaE.py](eliminaE.py) | Borra solo la primera aparición de un elemento | `eliminaE(3, [5,3,2,3])` → `[5, 2, 3]` |
| [eliminatodo.py](eliminatodo.py) | Borra todas las apariciones de un elemento | `eliminatodo(3, [5,3,2,3,4,3])` → `[5, 2, 4]` |

Las tres funciones son recursivas y tienen la misma estructura: el caso base es la lista vacía, y en cada llamada se revisa el primer elemento y se continúa con el resto de la lista (`lista[1:]`).

## Cómo ejecutarlos

Cada archivo trae sus pruebas al final e imprime los resultados:

```
python tomaintervalo.py
python eliminaE.py
python eliminatodo.py
```

## Observaciones

- `tomaintervalo` incluye las dos posiciones del intervalo. Por eso `tomaintervalo(2, 3, lista)` equivale a `lista[2:4]` en Python, y no a `lista[2:3]`, que excluye el final.
- En los ejemplos de `eliminaE`, a `print(eliminaE(3,[5,3,2,3])` le falta un paréntesis de cierre. En el archivo ya está corregido.
- En los ejemplos de `eliminatodo`, el resultado de `eliminatodo(4, [7,5,3,7,6])` aparece como `[]`. Como el 4 no está en la lista, el resultado correcto es la lista original, `[7, 5, 3, 7, 6]`.
