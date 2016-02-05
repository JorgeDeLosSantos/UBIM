Pyplot y lo básico
==================

En el Capítulo 2 vimos una introducción a `pylab`, un módulo de matplotlib que integra 
las utilidades gráficas del módulo `pyplot` y de la librería NumPy en un mismo *espacio de nombres*. 
El uso de `pylab` hace recordar mucho la sintaxis y la *filosofía de programación* de MATLAB. 
Por ello (y por razones que iremos conociendo posteriormente) en el entorno de Matplotlib es 
preferible utilizar `pyplot` y `NumPy` cómo módulos independientes, permitiendo una 
estructuración más limpia de código, diferenciando la parte de proceso de datos y la 
de graficación/visualización.

Un código típico utilizando pylab sería:

.. code:: python

	from pylab import *

	x = linspace(0,10)
	y = cos(x)

	plot(x,y,lw=2,ls="--")
	xlabel("Tiempo (s)")
	ylabel("Amplitud (mm)")
	show()


¿Y utilizando pyplot + NumPy?

.. code:: python

	import matplotlib.pyplot as plt
	import numpy as np

	x = np.linspace(0,10)
	y = np.cos(x)

	plt.plot(x,y,lw=2,ls="--")
	plt.xlabel("Tiempo (s)")
	plt.ylabel("Amplitud (mm)")
	plt.show()

Ambos códigos producen exactamente lo mismo. 

Ahora veremos una tercera forma (*mejorada*) de hacer lo anterior:

.. code:: python

	
	import matplotlib.pyplot as plt
	import numpy as np

	x = np.linspace(0,10)
	y = np.cos(x)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(x,y,lw=2,ls="--")
	ax.set_xlabel("Tiempo (s)")
	ax.set_ylabel("Amplitud (mm)")

	plt.show()


Y sí, en este texto vamos a utilizar esta *manera* de hacer las cosas, ¿la diferencia?: 
objetos, métodos y esas cosas propias de la programación orientada a objetos, que nos 
permitirá *organizar* nuestro código de una mejor manera, sobre todo cuando este 
tiende a ser extenso. De manera breve, lo que se hace es instanciar un objeto de 
la clase `Figure`, que es básicamente el objeto gráfico principal o lo que denominaríamos como 
*ventana*, y posteriormente se utilizan métodos de clase para crear un `Axes` y utilizar 
sus métodos para trazar la gráfica correspondiente y las etiquetas o leyendas necesarias.

Para las secciones siguientes se asumirá que en todo momento se han importado el módulo 
``pyplot`` y ``NumPy`` y que al final del código se ha incluido la instrucción 
``plt.show()`` para mostrar lo que se ha graficado.

.. code:: python

	import matplotlib.pyplot as plt
	import numpy as np
	# .
	# .
	# .
	plt.show()


Gráficas en coordenadas rectangulares
-------------------------------------

Hemos estado utilizando este tipo de gráficas en todos los ejemplos anteriores, entendemos 
por coordenadas rectangulares aquellas en donde cada punto del plano o espacio está dado 
por sus coordenadas (x,y) o (x,y,z) y las cuales hemos tenido *hasta en la sopa* desde nuestro 
primer curso de álgebra en el nivel secundario. Por ahora vamos a tomar el caso bidimensional, 
y en la mayoría de situaciones vamos a graficar un array que contiene los valores de la variable 
independiente (digamos *x*) contra un array que contiene los valores de la variable dependiente 
(digamos *f(x)*), utilizando, claro está, la función ``plot``.

Por ejemplo supongamos que queremos graficar la función :math:`f(x)=x^2 sin(x)` en el intervalo 
:math:`[0,2\pi]` 