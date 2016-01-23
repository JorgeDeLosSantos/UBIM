# -*- coding: utf-8 -*-
import os

source = "source"
build = "build"
instr = "sphinx-build -b latex "+source+" "+build
os.system(instr)
#os.startfile(build+r"\index.html")
