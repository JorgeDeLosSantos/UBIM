#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
	
__all__ = ["img_01",
		   "img_02",
		   "img_03",
		   "img_04",
		   "img_05",
		   "img_06",
		   "img_07"]

def img_01():
	x = np.linspace(0,10)
	y = np.cos(x)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(x, y)
	
	plt.savefig("img_01.png")
	
def img_02():
	T = [50, 60, 70, 80, 90, 100, 110, 120]
	P = [12, 20, 33, 54, 90, 148, 244, 403]

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(T, P)
	ax.set_xlabel(u"Temperatura (°C)")
	ax.set_ylabel(u"Presión (KPa)")
	ax.set_title(u"Relación P-T")
	
	plt.savefig("img_02.png")


def img_03():
	x = np.linspace(0,10)
	y = np.cos(x)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(x, y, lw=2)
	ax.plot(x, y+1, lw=4)
	ax.plot(x, y+2, linewidth=6)
	
	plt.savefig("img_03c.png")
	
def img_04():
	theta = np.linspace(0,2*np.pi,1000)
	r = 0.25*np.cos(3*theta)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="polar")

	ax.plot(theta, r)
	
	plt.savefig("img_04.png")
	
	
def img_05():pass
def img_06():pass
def img_07():pass
def img_08():pass

if __name__=='__main__':
	[eval(fun+"()") for fun in __all__]
