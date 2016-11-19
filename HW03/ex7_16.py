#!/usr/bin/python

from pylab import *

xvalues, yvalues = meshgrid(arange(0, 3, 0.1), arange(0, 3, 0.1))

r = 1.1

xdot = - xvalues + r + xvalues * yvalues - xvalues * xvalues
ydot = yvalues * (1 - yvalues)

streamplot(x=xvalues, y=yvalues, u=xdot, v=ydot)

show()
