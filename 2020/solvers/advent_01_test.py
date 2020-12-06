import solvers.advent_01_1 as advent_01_1
import solvers.advent_01_2 as advent_01_2

input = [
    '1721',
    '979',
    '366',
    '299',
    '675',
    '1456',
  ]

def test_1():
  assert advent_01_1.solve(input) == 514579
  
def test_2():
  assert advent_01_2.solve(input) == 241861950
