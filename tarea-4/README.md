# Tarea 4: programación recursiva (mínimo y quita)

Alumna: Marysol Segueda
Materia: Matemáticas Computacionales

Video con la explicación:
- (pendiente)

## Programas

| Archivo | Qué hace | Ejemplo |
|---|---|---|
| [minimo.py](minimo.py) | Regresa el elemento más pequeño de una lista de números | `minimo([6,7,2,7,5,4,2])` → `2` |
| [quita.py](quita.py) | Quita los primeros `n` elementos de una lista | `quita(3, [6,7,2,7,5,4,2])` → `[7, 5, 4, 2]` |

Las dos funciones son recursivas, igual que en la tarea 3: en cada llamada se trabaja con el primer elemento y se continúa con el resto de la lista (`lista[1:]`).

- `minimo` compara el primer elemento con el mínimo del resto y se queda con el más pequeño. El caso base es una lista de un solo elemento, que es su propio mínimo.
- `quita` descarta el primer elemento y vuelve a llamarse con `n - 1`. Se detiene cuando `n` llega a 0 (regresa lo que queda) o cuando la lista se vacía (regresa `[]`).

## Cómo ejecutarlos

Cada archivo trae sus pruebas al final e imprime los resultados:

```
python minimo.py
python quita.py
```

## Observaciones

- El enunciado de `minimo` no trae ejemplos. Los de las pruebas son míos, y cubren negativos, decimales y una lista de un solo elemento.
- Una lista vacía no tiene mínimo. En ese caso `minimo([])` regresa `None` en lugar de marcar error.
- En `quita`, si `n` es mayor que el tamaño de la lista, el resultado es la lista vacía, como pide el enunciado: `quita(10, [6,7,2,7,5,4,2])` → `[]`.
