from collections import defaultdict
import math

def load_test_wires(test_set):
  test_wires = [
    [
      'R8,U5,L5,D3'.split(','),
      'U7,R6,D4,L4'.split(',')
    ],
    [
      'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
      'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
    ]
  ]
  return test_wires[test_set]

def load_wires():
  with open('input') as data:
    return [ l.rstrip('\n').split(',') for l in data.readlines() ]

def map_wires(wires):
  axis_lookup = {
    'U': 'y',
    'D': 'y',
    'L': 'x',
    'R': 'x'
  }
  step_lookup = {
    'U': 1,
    'D': -1,
    'L': -1,
    'R': 1
  }
  
  grid_wire = defaultdict(set)
  grid_length = defaultdict(int)

  wire_pointer = 0
  for wire in wires:
    grid_pointer = (0, 0)
    wire_length = 0
    for instruction in wire:
      direction = instruction[0]
      axis = axis_lookup[direction]
      step = step_lookup[direction]
      value = (int(instruction[1:]) + 1) * step
      
      x, y = grid_pointer
      if axis == 'x':
        for x in range(x, x + value, step):
          grid_pointer = (x,y)
          grid_wire[grid_pointer].add(wire_pointer)
          if grid_length[grid_pointer] == 0:
            grid_length[grid_pointer] += wire_length
          wire_length += 1
      elif axis == 'y':
        for y in range(y, y + value, step):
          grid_pointer = (x,y)
          grid_wire[grid_pointer].add(wire_pointer)
          if grid_length[grid_pointer] == 0:
            grid_length[grid_pointer] += wire_length
          wire_length += 1
    wire_pointer += 1
  
  return { 'wire': grid_wire, 'length': grid_length }

def distance_from_origin(point):
  x, y = point
  return math.fabs(x) + math.fabs(y)

is_intersection = lambda point: len(grid[point]) == 2
find_distance = lambda point: (distance_from_origin(point), point)

if __name__ == "__main__":
  wires = load_test_wires(0)
  grid = map_wires(wires)

  intersections = filter(is_intersection, grid['wire'])
  distances = map(find_distance, intersections)
  distances = list(distances)
  distances.sort()

  print(distances[1])
