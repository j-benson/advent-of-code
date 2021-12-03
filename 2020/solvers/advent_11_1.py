from copy import deepcopy

def solve(input):
  waiting_area = WaitingArea(input)
  print(waiting_area)
  waiting_area.next_round()
  print(waiting_area)

class WaitingArea:
  def __init__(self, layout):
    self.round = 0
    self.layout = [ [ Tile(i) for i in row ] for row in layout ]

  def next_round(self):
    snapshot = deepcopy(self.layout)
    for r in range(len(snapshot)):
      for i in range(len(snapshot[r])):
        tile = snapshot[r][i]
        tile_before = snapshot[r][i-1] if i > 0 else Tile('-')
        tile_after = snapshot[r][i+1] if i < len(snapshot) - 1 else Tile('-')
        if tile.is_seat() and tile.is_empty():
          if not tile_before.is_occupied() and not tile_after.is_occupied():
            self.layout[r][i].sit()
        elif tile.is_seat() and tile.is_occupied():
          pass   
    self.round += 1
  
  def __str__(self):
    s  =  '----------\n'
    s += f' Round {self.round}\n'
    s +=  '----------\n'
    for row in self.layout:
      for i in row:
        s +=  str(i)
      s += '\n'
    return s
  
  def __repr__(self):
    return self.layout

  def __eq__(self, other):
    return self.layout == other.layout

class Tile:
  OCCUPIED_SEAT = '#'
  EMPTY_SEAT = 'L'
  FLOOR = '.'

  def __init__(self, value):
    self.value = value

  def is_seat(self):
    return self.value == self.EMPTY_SEAT or self.value == self.OCCUPIED_SEAT
  
  def is_occupied(self):
    return self.value == self.OCCUPIED_SEAT

  def is_empty(self):
    return self.value == self.EMPTY_SEAT

  def sit(self):
    if self.is_seat():
      self.value = self.OCCUPIED_SEAT

  def __str__(self):
    return self.value

  def __repr__(self):
    return self.__str__()

  def __eq__(self, other):
    self.value == other.value
