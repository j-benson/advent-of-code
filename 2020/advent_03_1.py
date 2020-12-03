def solve(input):
  map = Map(input)
  line = Line()
  
  trees = 0
  while(True):
    position = line.next()
    if not map.is_in_map_bounds(position): break
    if map.is_tree(position): trees += 1

  return trees

class Line:
  def __init__(self):
    self.x = 0
    self.y = 0

  def next(self):
    position = (self.x, self.y)
    self.y += 1
    self.x += 3
    return position

class Map:
  def __init__(self, input):
    self.lines = []
    for i in input:
      self.lines.append(MapLine(i))

  def is_in_map_bounds(self, position):
    _,y = position
    return y < len(self.lines)

  def is_tree(self, position):
    x, y = position
    return self.lines[y].is_tree(x)

class MapLine:
  def __init__(self, line):
    self.line = line
  
  def is_tree(self, position):
    return self.line[position % len(self.line)] == '#'
