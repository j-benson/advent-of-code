import re
from solvers.advent_07_1 import Rule

def solve(input):
  rules = [ Rule(item) for item in input ]
  bags = { rule.bag: rule for rule in rules }
  
  return count_bags(bags, 'shiny gold')

def count_bags(bags, bag, count=0):
  rule = bags[bag]
  if not rule.can_contain_bags():
    return 0
  child_count = 0
  for child_bag in rule.contains:
    num = rule.number_of_bags(child_bag)
    num_child = count_bags(bags, child_bag, child_count)
    child_count += num + (num * num_child)
  return child_count
  