def solve(input):
  map = Map(input)
  return map.number_of_trees(Line(1,1)) \
    * map.number_of_trees(Line(3,1)) \
    * map.number_of_trees(Line(5,1)) \
    * map.number_of_trees(Line(7,1)) \
    * map.number_of_trees(Line(1,2))

class Line:
  def __init__(self, change_x, change_y):
    self.x = 0
    self.y = 0
    self.slope = (change_x, change_y)

  def next(self):
    position = (self.x, self.y)
    change_x, change_y = self.slope
    self.y += change_y
    self.x += change_x
    return position

class Map:
  def __init__(self, input):
    self.lines = []
    for i in input:
      self.lines.append(MapLine(i))

  def number_of_trees(self, line):
    trees = 0
    while(True):
      position = line.next()
      if not self.is_in_map_bounds(position): break
      if self.is_tree(position): trees += 1

    return trees

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
