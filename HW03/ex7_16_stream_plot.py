#!/usr/bin/python

from pylab import *

xvalues, yvalues = meshgrid(arange(-3, 3, 0.1), arange(-3, 3, 0.1))
# xvalues, yvalues = meshgrid(arange(-1.5, -0.5, 0.1), arange(0.5, 1.5, 0.1))
# xvalues, yvalues = meshgrid(arange(-.1, .1, 0.01), arange(-.1, .1, 0.01))
r = 3
# r = 0

xdot = - xvalues + r + xvalues * yvalues - xvalues * xvalues
ydot = yvalues * (1 - yvalues)

streamplot(x=xvalues, y=yvalues, u=xdot, v=ydot)

show()
