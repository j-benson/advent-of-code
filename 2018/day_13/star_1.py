import time

class Map():
  NORTH = "^"
  SOUTH = "v"
  EAST = ">"
  WEST = "<"
  COMPASS = [NORTH, EAST, SOUTH, WEST]

  def __init__(self, map_file):
    self.carts = []
    self.tracks = dict()

    with open(map_file) as data:
      lines = data.readlines()
    y = 0
    for l in lines:
      x = 0
      for i in range(0, len(l)):
        if l[i] == "\n":
          continue
        if l[i] == self.EAST or l[i] == self.WEST:
          t = Track("-", (x, y), self)
          self.tracks[(x, y)] = t 
          self.carts.append(Cart(l[i], t))
        elif l[i] == self.NORTH or l[i] == self.SOUTH:
          t = Track("|", (x, y), self)
          self.tracks[(x, y)] = t
          self.carts.append(Cart(l[i], t))
        elif l[i] != " ":
          self.tracks[(x, y)] = Track(l[i], (x, y), self)
        x += 1
      y += 1

  def tick(self):
    for cart in self.carts:
      cart.tick()
    
  def collisions(self):
    collisions = []
    cart_positions = set()
    for cart in self.carts:
      if cart.track.position in cart_positions:
        collisions.append(cart)
      else:
        cart_positions.add(cart.track.position)
    return collisions

  def show(self):
    m = ""
    carts = { c.track.position:c for c in self.carts }
    max_y = sorted(self.tracks, key=lambda i:i[1], reverse=True)[0][1] + 1
    max_x = sorted(self.tracks, key=lambda i:i[0], reverse=True)[0][0] + 1
    for y in range(0, max_y):
      for x in range(0, max_x):
        m += carts[(x, y)].cart if (x, y) in carts else self.tracks[(x, y)].mark if (x, y) in self.tracks else " "
      m += "\n"
    print(m[:-1])
    
class Track():
  STRAIGHT_Y = "|"
  STRAIGHT_X = "-"
  CURVE_1 = "/"
  CURVE_2= "\\"
  INTERSECTION= "+"
  CURVE_PAIRS = {
      CURVE_1: [
        (Map.NORTH, Map.EAST),
        (Map.SOUTH, Map.WEST)
      ],
      CURVE_2: [
        (Map.NORTH, Map.WEST),
        (Map.SOUTH, Map.EAST)
      ]
    }

  def __init__(self, mark, position, map):
    self.mark = mark
    self.position = position
    self.map = map

  def __repr__(self):
    return "{}[{}]".format(self.position, self.mark)

  def north(self):
    x, y = self.position
    return map.tracks[(x, y - 1)]

  def south(self):
    x, y = self.position
    return map.tracks[(x, y + 1)]
    
  def east(self):
    x, y = self.position
    return map.tracks[(x + 1, y)]

  def west(self):
    x, y = self.position
    return map.tracks[(x - 1, y)]

class Cart():
  def __init__(self, cart, track):
    self.cart = cart
    self.track = track
    self.intersection_choice = 0
    self.intersection_choices = [self.turn_left, self.straight_over, self.turn_right]

  def __repr__(self):
    return "{}: {}".format(self.track, self.cart)

  def tick(self):
    self.move()
    self.change_direction()

  def move(self):
    if self.cart == Map.NORTH:
      self.track = self.track.north()
    elif self.cart == Map.SOUTH:
      self.track = self.track.south()
    elif self.cart == Map.EAST:
      self.track = self.track.east()
    elif self.cart == Map.WEST:
      self.track = self.track.west()

  def change_direction(self):
    if self.track.mark == Track.CURVE_1 or self.track.mark == Track.CURVE_2:
      self.turn_curve(self.track.mark)
    elif self.track.mark == Track.INTERSECTION:
      self.navigate_intersection()
  
  def turn_curve(self, curve):
    for pair in Track.CURVE_PAIRS[curve]:
      if self.cart == pair[0]:
        self.cart = pair[1]
      elif self.cart == pair[1]:
        self.cart = pair[0]

  def navigate_intersection(self):
    self.intersection_choices[self.intersection_choice]()
    self.intersection_choice += 1
    if self.intersection_choice == len(self.intersection_choices):
      self.intersection_choice = 0

  def turn_left(self):
    for i, compass in enumerate(Map.COMPASS):
      if self.cart == compass:
        self.cart = Map.COMPASS[i - 1]
        break

  def turn_right(self):
    for i, compass in enumerate(Map.COMPASS):
      if self.cart == compass:
        self.cart = Map.COMPASS[i + 1] if i + 1 < len(Map.COMPASS) else Map.COMPASS[0]
        break

  def straight_over(self):
    pass


map = Map("data.txt")
# map.show()
while True:
  # time.sleep(1)
  map.tick()
  # map.show()
  collisions = map.collisions()
  if collisions:
    print(collisions)
    break
