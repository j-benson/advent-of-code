def load_modules():
  with open('input') as data:
    return [ int(m.rstrip('\n')) for m in data.readlines() ]

def module_fuel(mass):
  return int(mass / 3) - 2

total_fuel = sum(map(module_fuel, load_modules()))
print(total_fuel)
