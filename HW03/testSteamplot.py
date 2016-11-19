#!/usr/bin/python

from pylab import *

xvalues, yvalues = meshgrid(arange(0, 3, 0.1), arange(0, 3, 0.1))

xdot = xvalues - xvalues * yvalues
ydot = - yvalues + xvalues * yvalues

streamplot(x=xvalues, y=yvalues, u=xdot, v=ydot)

show()
