GRID_SERIAL_NUMBER = 8868
FUEL_TANK_SIZE = 300
FUEL_TANK_RANGE = range(1, FUEL_TANK_SIZE + 1)
SEGMENT_SIZE = 3
SEGMENT_RANGE = range(0, SEGMENT_SIZE)

def rack_id(x):
  return x + 10

def power_level(rack_id, y):
  power = rack_id * y
  power = power + GRID_SERIAL_NUMBER
  power = power * rack_id
  if power > 99:
    power = int(str(power)[-3])
  else:
    power = 0
  return power - 5

def create_fuel_tank():
  fuel = dict()
  s = FUEL_TANK_SIZE + 1
  for x in FUEL_TANK_RANGE:
    for y in FUEL_TANK_RANGE:
      fuel[(x, y)] = power_level(rack_id(x), y)
  return fuel
  
def segment_fuel_tank(fuel_tank):
  segments = []
  for x in FUEL_TANK_RANGE:
    for y in FUEL_TANK_RANGE:
      segment_id = (x, y)
      if x + SEGMENT_SIZE - 1 > FUEL_TANK_SIZE or y + SEGMENT_SIZE - 1 > FUEL_TANK_SIZE:
        continue
      segments.append((segment_id, calc_segment_power(fuel_tank, segment_id)))
  return segments
          
def calc_segment_power(fuel_tank, segment_id):
  power = 0
  x, y = segment_id
  for sx in SEGMENT_RANGE:
    for sy in SEGMENT_RANGE:
      power += fuel_tank[(x+sx, y+sy)]
  return power


fuel_tank = create_fuel_tank()
segments = segment_fuel_tank(fuel_tank)

print(sorted(segments, key=lambda i:i[1], reverse=True)[0])
