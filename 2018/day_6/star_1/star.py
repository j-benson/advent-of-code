from math import fabs

manhattan_distance = lambda p, q : int(fabs(p[0] - q[0])) + int(fabs(p[1] - q[1]))

class Grid():
  def __init__(self, locations_filename):
    self.locations = self.load_locations(locations_filename)
    self.grid_size(self.locations)
    self.init_grid()
    self.map_manhattan_distances(self.locations)
    self.mark_grid()
    
  def load_locations(self, filename):
    with open(filename) as data:
      strip_new_line = lambda line : line[:-1] if line.endswith('\n') else line
      split = lambda line: line.split(", ")
      location_tuple = lambda arr : (int(arr[0]), int(arr[1]))
      return [location_tuple(split(strip_new_line(line))) for line in data.readlines()]

  def grid_size(self, locations):
    x_sorted = sorted(locations, reverse=True, key=lambda i : i[0])
    self.width = x_sorted[0][0] + 1
    y_sorted = sorted(locations, reverse=True, key=lambda i : i[1])
    self.height = y_sorted[0][1] + 1

  def init_grid(self):
    self.grid = dict()
    for x in range(0, self.width):
      for y in range(0, self.height):
        self.grid[(x, y)] = []

  def map_manhattan_distances(self, locations):
    # For each location find manhattan distance to every other point on the grid
    for l_x, l_y in locations:
      for g_x in range(0, self.width):
        for g_y in range(0, self.height):
          d = manhattan_distance((l_x, l_y), (g_x, g_y))
          # Update the grid with the distance to this location
          self.grid[(g_x, g_y)].append(((l_x, l_y), d))

  def mark_grid(self):
    self.marked_grid = dict() # ( grid_coordinate ) -> ( closest_location )
    self.edge_locations = set()

    for x in range(0, self.width):
      for y in range(0, self.height):
        location_distances = self.grid[(x, y)]
        location_distances.sort(key=lambda i : i[1])
        # Mark grid with closest location or None if more than one point have equal closest distance
        closest_location = location_distances[0][0] if location_distances[0][1] != location_distances[1][1] else None
        self.marked_grid[(x, y)] = closest_location
        
        # Locations on the edge of the grid are infinitely large.
        max_x = self.width - 1
        max_y = self.height - 1
        if x == 0 or y == 0 or x == max_x or y == max_y:
          self.edge_locations.add(closest_location)
  
def list_areas_by_size(grid):
  location_to_point_count = dict()
  for x in range(0, grid.width):
    for y in range(0, grid.height):
      p = grid.marked_grid[(x, y)]
      if p is None: continue
      location_to_point_count[p] = location_to_point_count[p] + 1 if p in location_to_point_count else 1
  location_to_point_count = [(p, location_to_point_count[p]) for p in location_to_point_count]
  location_to_point_count.sort(reverse=True, key=lambda i : i[1])

  for l in location_to_point_count:
      if l[0] not in grid.edge_locations:
        print("{} - {}".format(l[0], l[1])) 


if __name__ == "__main__":
    data = '../data.txt'
    # data = '../data_test.txt'

    grid = Grid(data)

    list_areas_by_size(grid)

  