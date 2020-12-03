import advent_02_1, advent_02_2

input = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
  ]

def test_1():
  assert advent_02_1.solve(input) == 2

def test_2():
  assert advent_02_2.solve(input) == 1
