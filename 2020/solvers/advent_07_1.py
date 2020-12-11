import re

def solve(input):
  rules = [ Rule(item) for item in input ]
  bags = { rule.bag: rule for rule in rules }
  
  good_bags = set()
  for bag in bags.keys():
    if search(bags, bag, 'shiny gold'):
      good_bags.add(bag)

  return len(good_bags)

def search(bags, bag, search_term):
  rule = bags[bag]
  if not rule.can_contain_bags():
    return False

  if rule.can_contain_bag(search_term):
    return True

  return True in list(map(lambda child: search(bags, child, search_term), rule.contains))

bag_colour_pattern = re.compile(r'\s*([0-9]*)\s*([\w\s]+)bags?')
class Rule:
  def __init__(self, value):
    s = value.split('contain')
    self.bag = self._extract_color(s[0])
    self.contains = { self._extract_color(item): self._extract_number(item) for item in s[1].split(',') }

  def _extract_color(self, value):
    try:
      return bag_colour_pattern.match(value).group(2).strip()
    except:
      raise Exception(f'No color for {value}')

  def _extract_number(self, value):
    try:
      return int(bag_colour_pattern.match(value).group(1).strip())
    except:
      return 0

  def can_contain_bag(self, value):
    return value in self.contains

  def can_contain_bags(self):
    return 'no other' not in self.contains

  def number_of_bags(self, bag=None):
    if bag is None:
      return sum(map(lambda i: self.contains[i], self.contains.keys()))
    return self.contains[bag]

  def __repr__(self):
    return f'Rule(bag=\'{self.bag}\', contains={str(self.contains)})'
