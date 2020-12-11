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
    'bright white': 1,
    'muted yellow': 2
  }
  assert Rule('bright white bags contain 1 shiny gold bag.').contains == {
    'shiny gold': 1
  }

def test_rule_can_contain_bags():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bags() == True
  assert Rule('bright white bags contain 1 shiny gold bag.').can_contain_bags() == True
  assert Rule('faded blue bags contain no other bags.').can_contain_bags() == False

def test_rule_can_contain_bag():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bag('bright white') == True
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bag('muted yellow') == True
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').can_contain_bag('shiny gold') == False

input_2 = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.',
  ]

def test_2():
  assert advent_07_2.solve(input_2) == 126

def test_2_1():
  assert advent_07_2.solve(input) == 32

def test_rule_number():
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').number_of_bags() == 3
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').number_of_bags('bright white') == 1
  assert Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.').number_of_bags('muted yellow') == 2
