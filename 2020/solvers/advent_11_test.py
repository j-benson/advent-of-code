import solvers.advent_11_1 as advent_11_1
import solvers.advent_11_2 as advent_11_2
from solvers.advent_11_1 import WaitingArea

input = [
  'L.LL.LL.LL',
  'LLLLLLL.LL',
  'L.L.L..L..',
  'LLLL.LL.LL',
  'L.LL.LL.LL',
  'L.LLLLL.LL',
  '..L.L.....',
  'LLLLLLLLLL',
  'L.LLLLLL.L',
  'L.LLLLL.LL',
]

def test_1():
  assert advent_11_1.solve(input) == 37

def test_round_1():
  waiting_area = WaitingArea(input)
  waiting_area.next_round()
  assert waiting_area.layout == WaitingArea([
    '#.##.##.##',
    '#######.##',
    '#.#.#..#..',
    '####.##.##',
    '#.##.##.##',
    '#.#####.##',
    '..#.#.....',
    '##########',
    '#.######.#',
    '#.#####.##',
  ]).layout

def test_round_2():
  waiting_area = WaitingArea(input)
  waiting_area.next_round()
  waiting_area.next_round()
  assert waiting_area == WaitingArea([
    '#.LL.L#.##',
    '#LLLLLL.L#',
    'L.L.L..L..',
    '#LLL.LL.L#'
    '#.LL.LL.LL',
    '#.LLLL#.##',
    '..L.L.....',
    '#LLLLLLLL#',
    '#.LLLLLL.L',
    '#.#LLLL.##',
  ])

def test_2():
  pass

