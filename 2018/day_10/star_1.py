import re
import time
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.animation as animation

p = re.compile(r"position=<\s*([-0-9]+),\s*([-0-9]+)> velocity=<\s*([-0-9]+),\s*([-0-9]+)>")

def read_data(data_file):
  with open(data_file) as data:
    find = lambda l : p.search(l)
    group = lambda m : ( (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4))) )
    create = lambda pv : Point(pv[0], pv[1])
    return [create(group(find(l))) for l in data.readlines()]

class Point():
  def __init__(self, position, velocity):
    self.position = position
    self.velocity = velocity

  def tick(self):
    x, y = self.position
    vx, vy = self.velocity
    self.position = (x+vx, y+vy)

def flip_y():
  bottom, top = plt.ylim()
  plt.ylim((top, bottom))

def tick():
  for p in points:
    p.tick()

def animate(i):
  tick()
  x, y = xy_points(points)
  ax.clear()
  ax.plot(x, y, marker="*", ls="")
  flip_y()

def fast_forward():
  for p in points:
    for i in range(0, 10117):
      p.tick() 
  
def xy_points(points):
  return ([ p.position[0] for p in points ], [ p.position[1] for p in points ])



points = read_data("data.txt")
fast_forward()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x, y = xy_points(points)
ax.plot(x, y, marker="*", ls="")
flip_y()

# ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
