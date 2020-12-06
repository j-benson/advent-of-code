import solvers.advent_05_1 as advent_05_1
import solvers.advent_05_2 as advent_05_2
from solvers.advent_05_1 import BoardingPass

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

# def test_2():
#   assert advent_05_2.solve(inputs.get_input(5))
