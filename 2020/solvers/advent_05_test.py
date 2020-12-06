import advent_05_1, advent_05_2
from advent_05_1 import BoardingPass

input = [
  'FBFBBFFRLR',
  'BFFFBBFRRR',
  'FFFBBBFRRR',
  'BBFFBBFRLL',
]

def test_1():
  assert advent_05_1.solve(input) == 820

def test_row():
  assert BoardingPass('FBFBBFFRLR').row == 44

def test_column():
  assert BoardingPass('FBFBBFFRLR').column == 5

def test_seat_id():
  assert BoardingPass('FBFBBFFRLR').seat_id == 357

def test_2():
  pass

