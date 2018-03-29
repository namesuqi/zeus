# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 每次产生一个新的坐标点
def data_gen():
  t = data_gen.t
  cnt = 0
  while cnt < 1000:
    cnt+=1
    t += 0.05
    if cnt%2==0:
        yield cnt, 0.9-cnt*0.001
    else:
        yield cnt, 0.9 - (cnt-1) * 0.001



# 因为run的参数是调用函数data_gen,
# 所以第一个参数可以不是framenum:设置line的数据,返回line
def run(data):
  # update the data
  t,y = data
  xdata.append(t)
  ydata.append(y)
  xmin, xmax = ax.get_xlim()
  if t >= xmax:
    ax.set_xlim(xmin+10, xmax+10)
    ax.figure.canvas.draw()
  line.set_data(xdata, ydata)
  line2.set_data(xdata, [x+1 for x in ydata])
  line3.set_data(xdata, [x + 2 for x in ydata])
  return line, line2, line3


if __name__ == "__main__":
  data_gen.t = 0

  # 绘图
  fig, ax = plt.subplots()
  line, = ax.plot([], [], lw=1)
  line2, = ax.plot([], [], lw=2)
  line3, = ax.plot([], [], lw=3)
  ax.set_ylim(0, 3)
  ax.set_xlim(0, 100)
  ax.grid()
  xdata, ydata = [], []
  # 每隔10秒调用函数run,run的参数为函数data_gen,
  # 表示图形只更新需要绘制的元素
  ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=100, repeat=False)
  plt.show()
