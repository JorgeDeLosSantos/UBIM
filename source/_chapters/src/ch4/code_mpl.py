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

	ax.plot(x,y,lw=2,ls="--")
	ax.set_xlabel("Tiempo (s)")
	ax.set_ylabel("Amplitud (mm)")
	
	plt.savefig("img_01.png")
	
	
def img_02():pass
def img_03():pass
def img_04():pass
def img_05():pass
def img_06():pass
def img_07():pass
def img_08():pass

if __name__=='__main__':
	[eval(fun+"()") for fun in __all__]
