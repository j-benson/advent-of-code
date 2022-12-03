from day3 import Rucksack, Item, Group

def test_rucksack():
  r = Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp')
  r.compartment_a.contents == 'vJrwpWtwJgWr'
  r.compartment_b.contents == 'hcsFMMfFFhFp'
  errors = r.find_error_items()
  assert errors[0].value == 'p'
  
  r = Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
  errors = r.find_error_items()
  assert errors[0].value == 'L'
  r = Rucksack('PmmdzqPrVvPwwTWBwg')
  errors = r.find_error_items()
  assert errors[0].value == 'P'
  r = Rucksack('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')
  errors = r.find_error_items()
  assert errors[0].value == 'v'
  r = Rucksack('ttgJtRGJQctTZtZT')
  errors = r.find_error_items()
  assert errors[0].value == 't'
  r = Rucksack('CrZsJsPPZsGzwwsLwLmpwMDw')
  errors = r.find_error_items()
  assert errors[0].value == 's'
  

def test_item():
  i = Item('a')
  assert i.priority() == 1
  i = Item('z')
  assert i.priority() == 26
  i = Item('A')
  assert i.priority() == 27
  i = Item('Z')
  assert i.priority() == 52

def test_group():
  g = Group()
  g.add_rucksack(Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp'))
  g.add_rucksack(Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'))
  g.add_rucksack(Rucksack('PmmdzqPrVvPwwTWBwg'))
  assert g.find_badge_item().value == 'r'

  g = Group()
  g.add_rucksack(Rucksack('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'))
  g.add_rucksack(Rucksack('ttgJtRGJQctTZtZT'))
  g.add_rucksack(Rucksack('CrZsJsPPZsGzwwsLwLmpwMDw'))
  assert g.find_badge_item().value == 'Z'
