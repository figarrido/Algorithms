# Algoritmos
Este repositorio contendrá ciertos algoritmos eficientes, descritos en el curso de [**'Diseño y Análisis de Algoritmos, Parte I'**](https://www.coursera.org/course/algo) dictado en [**Coursera**](https://www.coursera.org/).

Por el momento se tienen los algoritmos de:
- **MergeSort**: ordena listas desordenadas de números en tiempo O(n log n).
- **Invertion**: retorna una lista de tuplas con los valores en una lista que cumplan con la condición de `i < j` y `A[i] > A[j]`, siendo `i`, `j` índices de la lista y `A` la lista con valores en desorden. Trabaja en tiempo O(n log n).
- **CountInvertion**: retorna el número de elementos que cumplen con la condición de `Invertion`, para cantidades de datos considerables, si se quiere saber solo el número, este método es mas rápido que `Invertion`, ya que el espacio a utilizar es mucho menor. Trabaja en tiempo O(n log n).
- **QuickSort**: ordena listas desordenadas de números en tiempo promedio O(n log n) y espacio O(1).

Los algoritmos están desarrollados en [Python 3.4](https://www.python.org/download/releases/3.4.0/]).
