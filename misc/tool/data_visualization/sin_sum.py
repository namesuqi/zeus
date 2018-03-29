# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi-1, np.pi+1, 256, endpoint=True)
y1 = np.array([2.0 for i in range(256)])
y2 = np.sin(x) + 1
y3 = y1 - y2
ax = pl.subplot()
ax.set_ylim(0, 3)
pl.plot(x, y1, label="Total traffic")
pl.plot(x, y2, label="Background traffic")
pl.plot(x, y3, label="SDK traffic")
pl.legend()
pl.show()

