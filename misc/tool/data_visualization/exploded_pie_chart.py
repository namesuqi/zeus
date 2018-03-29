# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

from pylab import *


from pychart import *
import sys

data = [("foo", 10),("bar", 20), ("baz", 30), ("ao", 40)]

ar = area.T(size=(150,150), legend=legend.T(),
            x_grid_style = None, y_grid_style = None)

plot = pie_plot.T(data=data, arc_offsets=[0,10,0,10],
                  shadow = (20, -2, fill_style.gray50),
                  label_offset = 25,
                  arrow_style = arrow.a3)
ar.add_plot(plot)
ar.draw()