import solvers.advent_03_1 as advent_03_1
import solvers.advent_03_2 as advent_03_2

input = [
  '..##.......',
  '#...#...#..',
  '.#....#..#.',
  '..#.#...#.#',
  '.#...##..#.',
  '..#.##.....',
  '.#.#.#....#',
  '.#........#',
  '#.##...#...',
  '#...##....#',
  '.#..#...#.#',
]

def test_01():
  assert advent_03_1.solve(input) == 7

def test_02():
  assert advent_03_2.solve(input) == 336
  