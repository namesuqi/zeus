# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 1])
plt.ion()

for i in range(100):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.1)

