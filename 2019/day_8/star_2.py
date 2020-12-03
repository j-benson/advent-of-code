from collections import defaultdict
from star_1 import layers, width, height

image = defaultdict(lambda :2)

# Find pixel colour from layers
for layer in layers:
  for y in range(height): #row
    for x in range(width): #column
      layer_pixel = layer[y][x]
      if image[(x,y)] == 2:
        image[(x,y)] = layer_pixel

# Image 0,0 is top left
out = ''
for y in range(height):
  for x in range(width):
    out += 'X' if image[(x,y)] == 1 else ' '
  out += '\n'
print(out)
