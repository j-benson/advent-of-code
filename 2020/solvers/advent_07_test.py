import solvers.advent_07_1 as advent_07_1
import solvers.advent_07_2 as advent_07_2
from solvers.advent_07_1 import Rule

input = [
  'light red bags contain 1 bright white bag, 2 muted yellow bags.',
  'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
  'bright white bags contain 1 shiny gold bag.',
  'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
  'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
  'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
  'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
  'faded blue bags contain no other bags.',
  'dotted black bags contain no other bags.',
]

def test_1():
  assert advent_07_1.solve(input) == 4

def test_rule_bag():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').bag == 'light red'

def test_rule_contains():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').contains == {
    'bright white',
    'muted yellow'
  }
  assert Rule('bright white bags contain 1 shiny gold bag.').contains == {
    'shiny gold'
  }

def test_rule_can_contain_bags():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bags() == True
  assert Rule('bright white bags contain 1 shiny gold bag.').can_contain_bags() == True
  assert Rule('faded blue bags contain no other bags.').can_contain_bags() == False

def test_rule_can_contain_bag():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bag('bright white') == True
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bag('muted yellow') == True
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bag('shiny gold') == False

def test_2():
  pass

