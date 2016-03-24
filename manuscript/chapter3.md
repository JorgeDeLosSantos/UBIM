# Lo que hay que saber de NumPy

NumPy es una librería de de uso muy extendido en la comunidad técnico-científica de Python, 
es imprescindible y un estándar para situaciones en las cuales se manejan datos en 
forma de vectores o matrices.

Claro está que para graficar en Matplotlib no es estrictamente necesario utilizar arrays 
de NumPy, sino cualquier elemento iterable que pueda contener valores numéricos. Pero 
es evidente que los arrays de NumPy proporcionan una ventaja enorme cuando se manejan 
datos que requieren cierto procesamiento mediante herramientas matemáticas.

En este capítulo se tratarán funciones básicas de NumPy que permiten crear y modificar arrays, 
que luego se usarán para representarlos en Matplotlib.

## Creando arrays en Numpy

Primero, vamos a suponer que para todas las instrucciones subsecuentes, antes se ha importado 
el módulo NumPy utilizando el *alias* np, como sigue:

```python
>>> import numpy as np
```

La manera *básica* de crear un array es utilizando la función `np.array`, a la cual se debe 
pasar como argumento una lista de valores numéricos para definir un vector o bien una 
lista de listas para definir matrices, por ejemplo:

```python
>>> X=np.array([1,2,3])
```

Lo anterior crea un objeto de la clase `numpy.ndarray`

```python
>>> type(X)
<type 'numpy.ndarray'>
```

Para definir una matriz A dada por:

{$$}
A = \left(\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{matrix}\right)
{/$$}

se tiene que pasar una lista de listas como argumento, donde cada sublista representa una fila 
de la matriz:

```python
>>> A=np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> A
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

Esta es la forma *manual* de crear un array en NumPy, definiendo uno a uno los elementos, lo cual 
resultaría *pesado* en arreglos de grandes dimensiones. NumPy proporciona algunas funciones que 
permiten crear arrays con valores que siguen un patrón especifico, por ejemplo, valores en un intervalo 
{$$}[a,b]{/$$} con incrementos {$$}n{/$$}, o bien cierta cantidad de elementos en un rango, o incluso 
arreglos de ceros y unos.

La función que más usaremos en este texto será `linspace`, la cual permite crear un array de un 
cierto número de elementos en un intervalo fijo. Por ejemplo:

```python
>>> np.linspace(2,10,5)
array([  2.,   4.,   6.,   8.,  10.])
```

Lo anterior crea un array de 5 elementos en el intervalo {$$}[2,10]{/$$}.

Otra función muy similar es `arange`, la cual también necesita como argumentos los extremos del 
intervalo, pero en lugar del número de elementos se indica el paso o incremento.

```python
>>> np.arange(2,10,2)
array([2, 4, 6, 8])
```

Note que `arange` no incluye el extremo superior, es decir, toma los valores del intervalo abierto 
por la derecha {$$}[a,b){/$$}.