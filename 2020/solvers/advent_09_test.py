import solvers.advent_09_1 as advent_09_1
import solvers.advent_09_2 as advent_09_2

input = [
  '35',
  '20',
  '15',
  '25',
  '47',
  '40',
  '62',
  '55',
  '65',
  '95',
  '102',
  '117',
  '150',
  '182',
  '127',
  '219',
  '299',
  '277',
  '309',
  '576',
]

def test_1():
  assert advent_09_1.solve(input, 5) == 127

def test_2():
  pass

