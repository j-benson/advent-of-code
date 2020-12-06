import solvers.advent_06_1 as advent_06_1
import solvers.advent_06_2 as advent_06_2

input = [
  'abc',
  '',
  'a',
  'b',
  'c',
  '',
  'ab',
  'ac',
  '',
  'a',
  'a',
  'a',
  'a',
  '',
  'b',
]

def test_1():
  assert advent_06_1.solve(input) == 11

def test_2():
  assert advent_06_2.solve(input) == 6
