from collections import defaultdict

def load(version=None):
  filename = 'input' if version is None else f'input{version}'
  with open(filename) as data:
    return [ list(line.rstrip('\n')) for line in data.readlines() ]

has_asteroid = lambda m,p : m[p[1]][p[0]] == '#'

if __name__ == "__main__":
  space_map = load(1)
  width = len(space_map[0])
  height = len(space_map)
  
  # Map out Asteroids
  asteroid_map = set()
  for x in range(width):
    for y in range(height):
      if has_asteroid(space_map, (x, y)):
        asteroid_map.add((x, y))

  # Maths 😬
  candidate_asteroids = defaultdict(set)
  for canditate_asteroid in asteroid_map:
    for asteroid in asteroid_map:
      if asteroid == canditate_asteroid:
        continue

      xA, yA = canditate_asteroid
      xa, ya = asteroid

      gradient = None
      x = None
      if xA - xa == 0:
        x = yA - ya
      else:
        gradient = (yA - ya) / (xA - xa)

      can_see = True
      for other_asteroid in asteroid_map:
        if other_asteroid == canditate_asteroid \
          or other_asteroid == asteroid:
          continue

        xO, yO = other_asteroid
        if (gradient is not None and yO - yA == gradient * (xO - xA)) \
          or (x is not None and xO == xA):
          can_see = False
          break
      if can_see:
        candidate_asteroids[canditate_asteroid].add(asteroid)

# candidate_asteroids.sort(reversed=True)
  print(candidate_asteroids)
