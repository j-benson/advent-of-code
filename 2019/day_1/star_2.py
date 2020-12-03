def load_test_modules():
  return [ 1969 ]

def load_modules():
  with open('input') as data:
    return [ int(m.rstrip('\n')) for m in data.readlines() ]

mass_to_fuel = lambda mass: int(mass / 3) - 2

def module_fuel(mass):
  required_fuel = mass_to_fuel(mass)
  return required_fuel + fuel_for_fuel_mass(required_fuel)

def fuel_for_fuel_mass(mass):
  fuel = mass_to_fuel(mass)
  if fuel > 0:
    return fuel + fuel_for_fuel_mass(fuel)
  return 0

total_fuel = sum(map(module_fuel, load_modules()))
print(total_fuel)
