#!/usr/bin/env python3

import sys, input

class Rucksack:
  def __init__(self, contents) -> None:
    midpoint = int(len(contents) / 2)
    self.contents = contents
    self.compartment_a = Compartment(contents[:midpoint])
    self.compartment_b = Compartment(contents[midpoint:])

  def find_error_items(self):
    errors = []
    for a in self.compartment_a.contents:
      for b in self.compartment_b.contents:
        if a == b:
          errors.append(Item(a))
    return errors

class Compartment:
  def __init__(self, contents) -> None:
    self.contents = contents

class Item:
  def __init__(self, item) -> None:
    self.value = item

  def priority(self) -> int:
    item = ord(self.value)
    if item < ord('a'):
      return item - ord('A') + 27
    return item - ord('a') + 1

class Group:
  def __init__(self) -> None:
    self.MAX_SIZE = 3
    self.rucksacks = []
  
  def add_rucksack(self, rucksack) -> None:
    if len(self.rucksacks) >= self.MAX_SIZE:
      raise Exception('group full')
    self.rucksacks.append(rucksack)
  
  def find_badge_item(self) -> Item:
    sack_a_contents = list(self.rucksacks[0].contents)
    sack_b_contents = list(self.rucksacks[1].contents)
    sack_c_contents = list(self.rucksacks[2].contents)
    for a in sack_a_contents:
      if (a in sack_b_contents and a in sack_c_contents):
        return Item(a)
    raise Exception('badge not found')

if __name__ == '__main__':
  sacks = [ Rucksack(l) for l in input.to_list(sys.stdin.readlines()) ]
  error_items = map(lambda r: r.find_error_items()[0], sacks)
  priorities = map(lambda i: i.priority(), error_items)
  print(sum(priorities))

  groups = []
  group = Group()
  groups.append(group)
  while(len(sacks) > 0):
    try:
      group.add_rucksack(sacks[0])
      sacks.pop(0)
    except Exception:
      group = Group()
      groups.append(group)
  badge_items = map(lambda g: g.find_badge_item(), groups)
  badge_priorities = map(lambda i: i.priority(), badge_items)
  print(sum(badge_priorities))
