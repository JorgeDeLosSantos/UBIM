#-*- coding:utf-8 -*-
from pylab import *

__all__ = ["img_01",
		   "img_02",
		   "img_03",
		   "img_04",
		   "img_05",
		   "img_06",
		   "img_07"]

def img_01():
	plot([1,-2,5,-2,1,0,3])
	savefig('img_01.png')
	close()
	
def img_02():
	x = linspace(0,10)
	y = cos(x)
	plot(x,y)
	savefig('img_02.png')
	close()
	
def img_03():
	x = linspace(0,10)
	y = cos(x)
	plot(x,y,"ro")
	savefig('img_03.png')
	close()
	
def img_04():
	K = 525
	n = 0.2
	e = linspace(0,0.5)
	s = K*e**n;
	plot(e,s,'m')
	xlabel(u"Deformación (mm/mm)")
	ylabel(u"Esfuerzo (MPa)")
	savefig('img_04.png')
	close()
	
def img_05():
	K = 525
	n = 0.2
	e = linspace(0,0.5)
	s = K*e**n;
	plot(e,s,'m')
	xlabel(r"$\varepsilon$ (mm/mm)")
	ylabel(r"$\sigma$ (MPa)")
	title(r"Acero SAE 1008: $\sigma = K \varepsilon^n$")
	savefig('img_05.png')
	close()
	
def img_06():
	t = linspace(0,2)
	x = 12*t**3 - 18*t**2 + 2*t + 5
	v = diff(x)
	# Gráfica de posición
	subplot(2,1,1)
	plot(t,x,"b")
	ylabel(u"Posición (m)")
	# Gráfica de velocidad
	subplot(2,1,2)
	plot(t[:-1],v,"g")
	xlabel("Tiempo (s)")
	ylabel(u"Velocidad (m/s)")
	
	savefig('img_06.png')
	close()
	
def img_07():
	print "hola"

if __name__=='__main__':
	[eval(fun+"()") for fun in __all__]
