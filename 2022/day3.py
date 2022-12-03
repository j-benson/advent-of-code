#!/usr/bin/env python3

import sys, input

class Rucksack:
  def __init__(self, contents) -> None:
    midpoint = int(len(contents) / 2)
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

if __name__ == '__main__':
  sacks = [ Rucksack(l) for l in input.to_list(sys.stdin.readlines()) ]
  error_items = map(lambda r: r.find_error_items()[0], sacks)
  priorities = map(lambda i: i.priority(), error_items)
  print(sum(priorities))
